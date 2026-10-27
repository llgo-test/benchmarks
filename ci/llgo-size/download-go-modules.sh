#!/usr/bin/env bash
set -euo pipefail

# Retry downloads only: compiler failures must still fail immediately.
# Completed modules stay cached, so a retry only fetches missing downloads.
for attempt in 1 2 3; do
  if timeout --kill-after=30s 10m go mod download -x; then
    exit 0
  else
    status=$?
  fi
  if ((attempt == 3)); then
    echo "Go module download failed after $attempt attempts (exit $status)" >&2
    exit "$status"
  fi
  delay=$((attempt * 5))
  echo "Go module download failed (exit $status); retrying in ${delay}s ($attempt/3)" >&2
  sleep "$delay"
done
