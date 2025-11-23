export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'footer-max-line-length': [2, 'always', 100],
    'ai-attribution-exists': [2, 'always'],
    'subject-case': [2, 'always', ['lower-case']],
  },
  plugins: [
    {
      rules: {
        'ai-attribution-exists': ({ raw }) => {
          const aiAttributionPatterns = [
            /^Authored-by:\s+.+$/im,
            /^Commit-generated-by:\s+.+$/im,
            /^Assisted-by:\s+.+$/im,
            /^Co-authored-by:\s+.+$/im,
            /^Generated-by:\s+.+$/im,
          ];

          const hasValidFooter = aiAttributionPatterns.some((pattern) => pattern.test(raw));

          return [
            hasValidFooter,
            'Commit must include AI attribution footer:\n' +
              '  1. "Authored-by: [Human] <email>" - Human only, no AI\n' +
              '  2. "Commit-generated-by: [AI Tool] <email>" - Trivial AI (docs, msg, advice)\n' +
              '  3. "Assisted-by: [AI Tool] <email>" - AI helped, primarily human\n' +
              '  4. "Co-authored-by: [AI Tool] <email>" - 50/50 AI/human (40-60 leeway)\n' +
              '  5. "Generated-by: [AI Tool] <email>" - Majority AI generated',
          ];
        },
      },
    },
  ],
};
