#!/usr/bin/env bash
#
# Esbirrillo OS — installer entrypoint
#
# Walks the user through:
#   1. Pre-flight checks (Python, Claude CLI, git)
#   2. Choice of runtime (Hermes-agent vs Claude Code lite)
#   3. Choice of model + API keys
#   4. MCPs configuration
#   5. Vault location
#   6. First /setup-wizard run
#
# This is a SKELETON. Real logic lands in sem 1.

set -euo pipefail

KIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
USER_HOME="${HOME}"

cyan() { printf "\033[36m%s\033[0m\n" "$*"; }
green() { printf "\033[32m%s\033[0m\n" "$*"; }
yellow() { printf "\033[33m%s\033[0m\n" "$*"; }
red() { printf "\033[31m%s\033[0m\n" "$*"; }

banner() {
  cat <<'EOF'
  ┌─────────────────────────────────────────────┐
  │           Esbirrillo OS — install           │
  │  agentic personal OS, replicable, yours     │
  └─────────────────────────────────────────────┘
EOF
}

preflight() {
  cyan "→ Pre-flight checks"
  command -v python3 >/dev/null || { red "missing python3 (need 3.12+)"; exit 1; }
  command -v git >/dev/null || { red "missing git"; exit 1; }
  if ! command -v claude >/dev/null; then
    yellow "claude CLI not found. Install: https://docs.claude.com/en/docs/claude-code/quickstart"
    yellow "(continue anyway; you'll need it)"
  fi
  green "✓ basic deps present"
}

choose_runtime() {
  cyan "→ Choose runtime"
  cat <<EOF

  A) Hermes-agent (recommended, OSS, Nous Research)
     - Native cron scheduler
     - Multi-platform (Telegram/Discord/Slack/...)
     - Multi-model (any provider)
     - Lives at ~/.hermes/

  B) Claude Code + Telegram plugin (lite)
     - Simpler install
     - Telegram only
     - Uses Claude Code CronCreate

EOF
  read -rp "  Choice [A/B]: " runtime_choice
  runtime_choice="${runtime_choice:-A}"
  case "$runtime_choice" in
    A|a) RUNTIME="hermes" ;;
    B|b) RUNTIME="claude-code-telegram" ;;
    *)   red "invalid"; exit 1 ;;
  esac
  green "✓ runtime: $RUNTIME"
}

choose_model() {
  cyan "→ Choose model provider"
  cat <<EOF

  1) Anthropic (Claude — recommended for setup-wizard)
  2) OpenAI (GPT)
  3) Moonshot (Kimi)
  4) Nous Portal
  5) OpenRouter
  6) Other (you'll configure manually)

EOF
  read -rp "  Choice [1-6]: " model_choice
  green "✓ model choice: $model_choice (manual config required, see docs/INSTALL.md)"
}

setup_runtime() {
  cyan "→ Setup runtime"
  case "$RUNTIME" in
    hermes)
      yellow "TODO: ./bin/setup-hermes.sh"
      ;;
    claude-code-telegram)
      yellow "TODO: ./bin/setup-claude-telegram.sh"
      ;;
  esac
}

setup_mcps() {
  cyan "→ Setup MCPs"
  yellow "TODO: ./bin/setup-mcps.sh"
}

setup_vault() {
  cyan "→ Vault location"
  read -rp "  Vault path [~/Desktop/Esbirrillo Vault]: " vault_path
  vault_path="${vault_path:-${USER_HOME}/Desktop/Esbirrillo Vault}"
  mkdir -p "$vault_path"
  cp -R "${KIT_ROOT}/vault-template/." "${vault_path}/" 2>/dev/null || true
  green "✓ vault initialized at: $vault_path"
}

first_run_wizard() {
  cyan "→ Run /setup-wizard"
  cat <<EOF

  Open Claude Code in your kit directory:

    cd "$KIT_ROOT"
    claude

  Then run:

    /setup-wizard

  The wizard will interview you and build:
    - your context files (Personal, business, health, learning, finances)
    - your custom agents (CEO of X, Coach for Y, etc.)
    - your North Star + frameworks
    - your working memory
    - your Notion DBs (creates them in your workspace)

  Estimated time: 3-5h spread over 2-3 sessions.

EOF
}

main() {
  banner
  preflight
  choose_runtime
  choose_model
  setup_runtime
  setup_mcps
  setup_vault
  first_run_wizard
  green "✓ Esbirrillo OS skeleton installed at: $KIT_ROOT"
  cyan "  Next: cd \"$KIT_ROOT\" && claude → /setup-wizard"
}

main "$@"
