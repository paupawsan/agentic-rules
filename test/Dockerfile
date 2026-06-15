# Clean-room dogfood image for the Agentic Rules Framework.
#
# Builds a fresh, dependency-free Python environment, copies the framework in
# as a brand-new user would, and runs test/dogfood.sh end to end.
#
# Build (context = repo root):
#   docker build -f test/Dockerfile -t agentic-rules-dogfood .
# Run:
#   docker run --rm agentic-rules-dogfood
#
# The framework is stdlib-only, so no pip install step is needed — that is part
# of what this image verifies.

FROM python:3.12-slim

# Mirror a normal, non-root user environment. Create /framework owned by the
# non-root user first so the user can write bytecode/generated files into it
# (WORKDIR alone would create it root-owned).
RUN useradd --create-home tester && mkdir -p /framework && chown tester:tester /framework
WORKDIR /framework
COPY --chown=tester:tester . /framework
USER tester

ENTRYPOINT ["bash", "test/dogfood.sh"]
