import { describe, it, expect } from 'vitest';
import raiFooterExists from '../rules/rai-footer-exists.js';

const iterations = 10000;

describe('RAI Footer Validation Benchmark', () => {
  it('should validate AI-Generated footer', () => {
    const parsed = {
      raw: 'feat: add feature\n\n🛡️ RAI: AI-Generated',
    } as any;

    const start = performance.now();
    for (let i = 0; i < iterations; i++) {
      const result = raiFooterExists(parsed) as [boolean, string];
      expect(result).toBeDefined();
      expect(Array.isArray(result)).toBe(true);
      expect(result[0]).toBe(false);
    }
    const end = performance.now();

    console.log(`AI-Generated validation: ${iterations} iterations in ${(end - start).toFixed(2)}ms`);
    console.log(`Average: ${((end - start) / iterations).toFixed(4)}ms per validation`);
  });

  it('should validate AI-Assisted footer', () => {
    const parsed = {
      raw: 'fix: resolve bug\n\n🛡️ RAI: AI-Assisted',
    } as any;

    const start = performance.now();
    for (let i = 0; i < iterations; i++) {
      const result = raiFooterExists(parsed) as [boolean, string];
      expect(result).toBeDefined();
      expect(Array.isArray(result)).toBe(true);
      expect(result[0]).toBe(false);
    }
    const end = performance.now();

    console.log(`AI-Assisted validation: ${iterations} iterations in ${(end - start).toFixed(2)}ms`);
    console.log(`Average: ${((end - start) / iterations).toFixed(4)}ms per validation`);
  });

  it('should validate Verdent AI footer', () => {
    const parsed = {
      raw: 'chore: update\n\nGenerated-by: Verdent AI <verdent@verdent.ai>',
    } as any;

    const start = performance.now();
    for (let i = 0; i < iterations; i++) {
      const result = raiFooterExists(parsed) as [boolean, string];
      expect(result).toBeDefined();
      expect(Array.isArray(result)).toBe(true);
      expect(result[0]).toBe(true);
    }
    const end = performance.now();

    console.log(`Verdent AI validation: ${iterations} iterations in ${(end - start).toFixed(2)}ms`);
    console.log(`Average: ${((end - start) / iterations).toFixed(4)}ms per validation`);
  });

  it('should validate invalid footer', () => {
    const parsed = {
      raw: 'feat: add feature\n\nNo RAI footer',
    } as any;

    const start = performance.now();
    for (let i = 0; i < iterations; i++) {
      const result = raiFooterExists(parsed) as [boolean, string];
      expect(result).toBeDefined();
      expect(Array.isArray(result)).toBe(true);
      expect(result[0]).toBe(false);
    }
    const end = performance.now();

    console.log(`Invalid footer validation: ${iterations} iterations in ${(end - start).toFixed(2)}ms`);
    console.log(`Average: ${((end - start) / iterations).toFixed(4)}ms per validation`);
  });
});
