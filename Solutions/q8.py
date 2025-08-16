from ast import Name, Call
import bandit
from bandit.core import issue
from bandit.core import test_properties as test


@test.test_id("B1337")
@test.checks("Call")
def os_path_join(context):
    if (
    context.is_module_imported_like("os.path")
    and context.call_function_name == "join"
    and isinstance(context.node.args[-1], Name)
    ):
        return bandit.Issue(
                severity=bandit.LOW,
                confidence=bandit.HIGH,
                cwe=issue.Cwe.IMPROPER_INPUT_VALIDATION,
                text=f"Call to path.join with variable parameter (\"{context.node.args[-1].id}\")",
                lineno=context.get_lineno_for_call_arg(
                    "os.path.join"
                ),
            )