import { defineConfig } from 'vitest/config';

const REPORTS_DIR = 'reports';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['lcov', 'text'],
      reportsDirectory: REPORTS_DIR,
      include: ['src/**/*.ts'],
      exclude: ['tests/**/*.test.ts'],
    },
    reporters: [
      'default',
      [
        'junit',
        {
          outputFile: `${REPORTS_DIR}/junit-vitest.xml`,
        },
      ],
    ],
  },
});
