import { describe, it, expect } from 'vitest';
import { execSync } from 'child_process';
import { writeFileSync, unlinkSync } from 'fs';
import { join } from 'path';

describe('Integration Tests', () => {
  const testCommitFile = join(process.cwd(), '.test-commit-msg');

  const testCommit = (message: string): { exitCode: number; output: string } => {
    writeFileSync(testCommitFile, message);
    try {
      const output = execSync(`npx commitlint --edit ${testCommitFile}`, {
        encoding: 'utf-8',
        cwd: join(process.cwd(), '../..'),
      });
      return { exitCode: 0, output };
    } catch (error: any) {
      return { exitCode: error.status, output: error.stderr };
    } finally {
      try {
        unlinkSync(testCommitFile);
      } catch {}
    }
  };

  it('should accept valid AI-Generated footer', () => {
    const result = testCommit('feat: add new feature\n\n🛡️ RAI: AI-Generated');
    expect(result.exitCode).toBe(0);
  });

  it('should accept valid AI-Assisted footer', () => {
    const result = testCommit('fix: resolve bug\n\n🛡️ RAI: AI-Assisted');
    expect(result.exitCode).toBe(0);
  });

  it('should accept valid Verdent AI footer', () => {
    const result = testCommit(
      'chore: update deps\n\nGenerated-by: Verdent AI <verdent@verdent.ai>'
    );
    expect(result.exitCode).toBe(0);
  });

  it('should reject commit without RAI footer', () => {
    const result = testCommit('feat: add feature\n\nNo footer here');
    expect(result.exitCode).not.toBe(0);
    expect(result.output).toContain('RAI footer');
  });

  it('should reject commit with malformed footer', () => {
    const result = testCommit('feat: add feature\n\n🛡️ RAI: AI-Something');
    expect(result.exitCode).not.toBe(0);
  });

  it('should accept case-insensitive footer', () => {
    const result = testCommit('feat: add feature\n\n🛡️ rai: ai-generated');
    expect(result.exitCode).toBe(0);
  });

  it('should accept footer with additional text before it', () => {
    const result = testCommit(
      'feat: add feature\n\nSome description\n\nCloses #123\n\n🛡️ RAI: AI-Assisted'
    );
    expect(result.exitCode).toBe(0);
  });
});
