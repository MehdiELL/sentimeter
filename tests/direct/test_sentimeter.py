# Direct-mode unit tests for SentiMeter.  Run: pytest tests/direct/ -v
import json

CONTRACT = "contracts/sentimeter.py"


def test_submit_and_evaluate(direct_vm, direct_deploy, direct_alice):
    c = direct_deploy(CONTRACT)
    direct_vm.sender = direct_alice
    idx = c.submit("some example content to evaluate")
    assert int(idx) == 0
    direct_vm.mock_llm(r".*JSON.*", json.dumps({"label": "positive", "score": 80, "reasoning": "ok"}))
    c.evaluate(0)
    item = c.get_item(0)
    assert item["label"] == "positive"
    assert bool(item["done"]) is True


def test_evaluate_rejects_invalid_id(direct_vm, direct_deploy, direct_alice):
    c = direct_deploy(CONTRACT)
    direct_vm.sender = direct_alice
    with direct_vm.expect_revert("invalid item id"):
        c.evaluate(0)
