import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['lcov', 'text'],
      reportsDirectory: 'reports',
      include: ['src/**/*.ts'],
      exclude: ['src/**/*.test.ts'],
    },
    reporters: [
      'default',
      [
        'junit',
        {
          outputFile: 'reports/junit-vitest.xml',
        },
      ],
    ],
  },
});
