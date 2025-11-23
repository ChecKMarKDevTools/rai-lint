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
      return { exitCode: error.status, output: error.stderr || error.stdout || '' };
    } finally {
      try {
        unlinkSync(testCommitFile);
      } catch {
        // Ignore cleanup errors
      }
    }
  };

  it('should accept valid Generated-by footer', () => {
    const result = testCommit('feat: add new feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>');
    expect(result.exitCode).toBe(0);
  });

  it('should accept valid Assisted-by footer', () => {
    const result = testCommit('fix: resolve bug\n\nAssisted-by: Verdent AI <verdent@verdent.ai>');
    expect(result.exitCode).toBe(0);
  });

  it('should accept valid Verdent AI footer', () => {
    const result = testCommit('chore: update deps\n\nGenerated-by: Verdent AI <verdent@verdent.ai>');
    expect(result.exitCode).toBe(0);
  });

  it('should reject commit without AI attribution footer', () => {
    const result = testCommit('feat: add feature\n\nNo footer here');
    expect(result.exitCode).not.toBe(0);
    expect(result.output).toContain('AI attribution');
  });

  it('should accept case-insensitive footer', () => {
    const result = testCommit('feat: add feature\n\ngenerated-by: GitHub Copilot <copilot@github.com>');
    expect(result.exitCode).toBe(0);
  });

  it('should accept footer with additional text before it', () => {
    const result = testCommit(
      'feat: add feature\n\nSome description\n\nCloses #123\n\nGenerated-by: GitHub Copilot <copilot@github.com>'
    );
    expect(result.exitCode).toBe(0);
  });
});
