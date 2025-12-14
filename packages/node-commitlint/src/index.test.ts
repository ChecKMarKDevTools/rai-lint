import { describe, it, expect } from 'vitest';
import plugin from './index';

describe('plugin export', () => {
  it('should export a valid commitlint plugin', () => {
    expect(plugin).toBeDefined();
    expect(plugin.rules).toBeDefined();
    expect(plugin.rules['rai-footer-exists']).toBeDefined();
  });

  it('should have rai-footer-exists rule', () => {
    const rule = plugin.rules['rai-footer-exists'];
    expect(typeof rule).toBe('function');
  });
});
