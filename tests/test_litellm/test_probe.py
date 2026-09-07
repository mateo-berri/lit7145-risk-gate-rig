from litellm.llms.anthropic.probe import transform


def test_transform():
    assert transform(1) == 2
