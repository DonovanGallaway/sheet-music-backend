"""CreateSheetsTable Migration."""

from masoniteorm.migrations import Migration


class CreateSheetsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("sheets") as table:
            table.increments("id")
            table.string('name')
            table.string('instrumentation')
            table.string('link')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("sheets")
