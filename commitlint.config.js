export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'footer-max-line-length': [0],
    'rai-footer-exists': [2, 'always'],
  },
  plugins: [
    {
      rules: {
        'rai-footer-exists': ({ raw }) => {
          const raiFooterPattern = /^Generated-by:\s+Verdent AI\s+<verdent@verdent\.ai>$/m;
          const hasRaiFooter = raiFooterPattern.test(raw);
          
          return [
            hasRaiFooter,
            'Commit must include RAI footer: "Generated-by: Verdent AI <verdent@verdent.ai>"',
          ];
        },
      },
    },
  ],
};
