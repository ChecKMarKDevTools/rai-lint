import { describe, it, expect } from 'vitest';
import raiFooterExists from './rai-footer-exists.js';

describe('rai-footer-exists', () => {
  it('should pass with AI-Generated footer', () => {
    const parsed = {
      raw: 'feat: add new feature\n\n🛡️ RAI: AI-Generated',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should pass with AI-Assisted footer', () => {
    const parsed = {
      raw: 'fix: resolve bug\n\n🛡️ RAI: AI-Assisted',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should pass with Verdent AI footer', () => {
    const parsed = {
      raw: 'chore: update dependencies\n\nGenerated-by: Verdent AI <verdent@verdent.ai>',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should fail without RAI footer', () => {
    const parsed = {
      raw: 'feat: add new feature\n\nSome other footer',
    } as any;

    const [isValid, message] = raiFooterExists(parsed);
    expect(isValid).toBe(false);
    expect(message).toContain('RAI footer');
  });

  it('should pass with case-insensitive footer', () => {
    const parsed = {
      raw: 'feat: add feature\n\n🛡️ rai: ai-generated',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(true);
  });

  it('should fail with malformed footer', () => {
    const parsed = {
      raw: 'feat: add feature\n\n🛡️ RAI: AI-Something',
    } as any;

    const [isValid] = raiFooterExists(parsed);
    expect(isValid).toBe(false);
  });
});
