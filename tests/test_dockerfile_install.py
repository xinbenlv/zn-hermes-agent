from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCKERFILE = REPO_ROOT / "Dockerfile"


def test_dockerfile_uses_uv_for_all_extras_install():
    content = DOCKERFILE.read_text(encoding="utf-8")

    assert 'pip install --no-cache-dir uv --break-system-packages' in content
    assert 'uv pip install --system -e ".[all]"' in content
    assert 'pip install --no-cache-dir -e ".[all]" --break-system-packages' not in content
