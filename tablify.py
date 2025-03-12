from prettytable import PrettyTable


class HighlightableTable:
    def __init__(self):
        self.table = PrettyTable()
        self.rows = []
        self.highlight_cells = []

        # Configure table structure
        self.table.field_names = ["bitnami_col1", "bitnami_col2",
                                  "confluentinc_col1", "confluentinc_col2"]
        self.table.header = False
        self.table.title = "bitnami          confluentinc"

    def add_row(self, row):
        """Add a row to the table (preserves original data)"""
        self.rows.append(row)

    def highlight(self, cells_to_highlight):
        """Set which cells to highlight (by exact text match)"""
        self.highlight_cells = cells_to_highlight

    def print_table(self):
        """Print the table with highlighted cells"""
        # ANSI styling configuration
        HIGHLIGHT_STYLE = "\033[92m"  # Green text
        RESET_STYLE = "\033[0m"

        # Create a copy of the table for display
        temp_table = PrettyTable()
        temp_table.field_names = self.table.field_names
        temp_table.header = False
        temp_table.title = self.table.title

        # Process rows with highlighting
        for row in self.rows:
            highlighted_row = [
                f"{HIGHLIGHT_STYLE}{cell}{RESET_STYLE}"
                if cell in self.highlight_cells
                else cell
                for cell in row
            ]
            temp_table.add_row(highlighted_row)

        print(temp_table)


# Usage example
if __name__ == "__main__":
    # Create and populate table
    table = HighlightableTable()
    table.add_row(["zookeeper", "kraft", "zookeeper", "kraft"])
    table.add_row(["GUI's", "GUI's", "GUI's", "GUI's"])

    # Highlight specific cells
    # List of cells to highlight
    table.highlight(["zookeeper", "confluentinc"])

    # Print the formatted table
    table.print_table()
