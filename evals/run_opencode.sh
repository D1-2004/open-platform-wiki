#!/bin/zsh
# 用 opencode 对 questions.jsonl 里的问题逐题答题，输出到 evals/runs/<日期>/。
# 用法: ./run_opencode.sh [core|extended|all] [qid ...]
#   ./run_opencode.sh              # 跑 core 集(默认)
#   ./run_opencode.sh all          # 全部
#   ./run_opencode.sh - q024 q113  # 只跑指定题
# 依赖: opencode CLI(任何配置好的模型)。经验教训(2026-08-11):
#   1) 必须前台跑、stdout 走管道——后台+文件重定向会静默挂起;
#   2) 加 --pure 跳过外部插件,否则可能被插件卡死;
#   3) cwd 必须是知识库根(opencode 非交互模式会自动拒绝 external_directory 权限)。
set -e
EVALS_DIR="$(cd "$(dirname "$0")" && pwd)"
WIKI="$(dirname "$EVALS_DIR")"
MODE="${1:-core}"
RUN_DIR="$EVALS_DIR/runs/$(date +%Y-%m-%d-%H%M)"
mkdir -p "$RUN_DIR"

cd "$WIKI"
python3 - "$EVALS_DIR/questions.jsonl" "$MODE" "${@:2}" <<'PYEOF' > "$RUN_DIR/_qids.txt"
import json, sys
qfile, mode, explicit = sys.argv[1], sys.argv[2], sys.argv[3:]
for line in open(qfile):
    q = json.loads(line)
    if explicit:
        if q['id'] in explicit: print(q['id'])
    elif mode == 'all' or q['set'] == mode:
        print(q['id'])
PYEOF

while read -r qid; do
  [ -z "$qid" ] && continue
  question=$(python3 -c "
import json
for l in open('$EVALS_DIR/questions.jsonl'):
    q=json.loads(l)
    if q['id']=='$qid': print(q['question']); break")
  prompt="钉钉开放平台知识库在 $WIKI，先读其中 AGENTS.md，再回答我的问题：

$question"
  echo "=== $qid $(date +%H:%M:%S) ==="
  opencode run --pure "$prompt" </dev/null 2>"$RUN_DIR/$qid.err" | cat > "$RUN_DIR/$qid.out"
  echo "$qid done bytes=$(wc -c < "$RUN_DIR/$qid.out")"
done < "$RUN_DIR/_qids.txt"
echo "答案在 $RUN_DIR/，判卷提示词见 evals/judge_prompt.md"
