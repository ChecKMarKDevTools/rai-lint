#!/bin/bash

set -e

echo "🚀 Setting up CheckMarK RAI Lint development environment..."
echo ""

if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js >= 16.0.0"
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python >= 3.9"
    exit 1
fi

echo "📦 Installing Node.js dependencies..."
npm install
echo "✅ Node.js dependencies installed"
echo ""

echo "📦 Installing Python dependencies..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate || . .venv/Scripts/activate
pip install --upgrade pip
pip install -e "packages/python-gitlint[dev]"
echo "✅ Python dependencies installed"
echo ""

echo "🔨 Building Node.js package..."
cd packages/node-commitlint
npm run build
cd ../..
echo "✅ Node.js package built"
echo ""

echo "🧪 Running tests..."
echo ""
echo "Node.js tests:"
cd packages/node-commitlint
npm test
cd ../..
echo ""
echo "Python tests:"
source .venv/bin/activate || . .venv/Scripts/activate
pytest packages/python-gitlint/tests -v
echo "✅ All tests passed"
echo ""

echo "✨ Setup complete! You're ready to develop."
echo ""
echo "Next steps:"
echo "  1. For Node development: cd packages/node-commitlint && npm test"
echo "  2. For Python development: source .venv/bin/activate && pytest packages/python-gitlint/tests"
echo "  3. Run benchmarks: npm test benchmarks/"
echo "  4. Install git hooks: npx lefthook install"
echo ""
