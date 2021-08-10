import json
from behave import given, when, then, step
from nose import tools


@given("the following users")
def step_init_users(context):
    users = [row.as_dict() for row in context.table]
    with open(f"{context.data_dir}/users.json", "w") as f:
        json.dump(users, f)
    for user in users:
        user_id = user["id"]
        with open(f"{context.data_dir}/user{user_id}.json", "w") as f:
            json.dump(user, f)


@when('I send "{method}" request to "{url}" endpoint')
def step_send_request(context, method, url):
    if method == "GET":
        context.response = context.client.get(url)
    else:
        raise NotImplementedError("Add if needed")


@then('I should receive the response with "{status_code}" status code and the following body')
def step_receive_response(context, status_code):
    # assert context.response.status_code == int(status_code)
    tools.assert_equal(context.response.status_code, int(status_code))
    tools.assert_dict_equal(context.response.json(), json.loads(context.text))
