export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'footer-max-line-length': [0],
    'ai-attribution-exists': [2, 'always'],
  },
  plugins: [
    {
      rules: {
        'ai-attribution-exists': ({ raw }) => {
          const aiAttributionPatterns = [
            /^Co-authored-by:\s+.+\s+<.+@.+>$/im,
            /^Assisted-by:\s+.+\s+<.+@.+>$/im,
            /^Generated-by:\s+.+\s+<.+@.+>$/im,
            /^Commit-generated-by:\s+.+\s+<.+@.+>$/im,
          ];
          
          const hasValidFooter = aiAttributionPatterns.some((pattern) => pattern.test(raw));
          
          return [
            hasValidFooter,
            'Commit must include AI attribution footer:\n' +
            '  - "Co-authored-by: [AI Tool] <email>" (34-66% AI)\n' +
            '  - "Assisted-by: [AI Tool] <email>" (up to 33% AI)\n' +
            '  - "Generated-by: [AI Tool] <email>" (67-100% AI)\n' +
            '  - "Commit-generated-by: [AI Tool] <email>" (message only)',
          ];
        },
      },
    },
  ],
};
