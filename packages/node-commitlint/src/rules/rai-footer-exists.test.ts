import { describe, it, expect } from 'vitest';
import raiFooterExists from './rai-footer-exists.js';

describe('rai-footer-exists', () => {
  it('should pass with Generated-by footer', () => {
    const parsed = {
      raw: 'feat: add new feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should pass with Assisted-by footer', () => {
    const parsed = {
      raw: 'fix: resolve bug\n\nAssisted-by: Verdent AI <verdent@verdent.ai>',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should pass with Co-authored-by footer', () => {
    const parsed = {
      raw: 'refactor: improve code\n\nCo-authored-by: GitHub Copilot <copilot@github.com>',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should pass with Commit-generated-by footer', () => {
    const parsed = {
      raw: 'chore: update dependencies\n\nCommit-generated-by: Claude AI <claude@anthropic.com>',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should fail without AI attribution footer', () => {
    const parsed = {
      raw: 'feat: add new feature\n\nSome other footer',
    } as any;

    const [isValid, message] = raiFooterExists(parsed);
    expect(isValid).toBe(false);
    expect(message).toContain('AI attribution');
  });

  it('should pass with case-insensitive footer', () => {
    const parsed = {
      raw: 'feat: add feature\n\ngenerated-by: GitHub Copilot <copilot@github.com>',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should fail with malformed footer', () => {
    const parsed = {
      raw: 'feat: add feature\n\nGenerated-by: Invalid Format',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(false);
  });

  it('should pass with multiple AI tools', () => {
    const parsed = {
      raw: 'feat: complex feature\n\nGenerated-by: ChatGPT <chatgpt@openai.com>',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });
});
