from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv
from cubes import Workspace

engine = create_engine('sqlite:///data.sqlite')
create_table_from_csv(engine,
                      "IBRD_Balance_Sheet__FY2010.csv",
                      table_name="ibrd_balance",
                      fields=[
                          ("category", "string"),
                          ("category_label", "string"),
                          ("subcategory", "string"),
                          ("subcategory_label", "string"),
                          ("line_item", "string"),
                          ("year", "integer"),
                          ("amount", "integer")],
                      create_id=True
                      )

workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("tutorial_model.json")

browser = workspace.browser("ibrd_balance")
result = browser.aggregate()
print(result.summary["record_count"], result.summary["amount_sum"])

result = browser.aggregate(drilldown=["year"])
for record in result:
    print(record)

result = browser.aggregate(drilldown=["item"])
for record in result:
    print(record)
