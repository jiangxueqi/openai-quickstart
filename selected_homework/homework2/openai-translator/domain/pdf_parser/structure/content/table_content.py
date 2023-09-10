import pandas as pd
from domain.pdf_parser.structure.content.content import Content
from domain.pdf_parser.structure.content.content_type import ContentType
from infrastructure.logger.logger import logger


class TableContent(Content):
    def __init__(self, data, translation=None):
        df = pd.DataFrame(data)

        # Verify if the number of rows and columns in the data and DataFrame object match
        if len(data) != len(df) or len(data[0]) != len(df.columns):
            raise ValueError(
                "The number of rows and columns in the extracted table data and DataFrame object do not match.")

        super().__init__(ContentType.TABLE, df)

    def set_translation(self, translation, status):
        try:
            if not isinstance(translation, str):
                raise ValueError(f"Invalid translation type. Expected str, but got {type(translation)}")

            logger.debug(f"[translation]\n{translation}")
            # Extract column names from the first set of brackets
            header = translation.split(']')[0][1:].split(', ')
            # Extract data rows from the remaining brackets
            data_rows = translation.split('] ')[1:]
            # Replace Chinese punctuation and split each row into a list of values
            data_rows = [row[1:-1].split(', ') for row in data_rows]
            # Create a DataFrame using the extracted header and data
            translated_df = pd.DataFrame(data_rows, columns=header)
            logger.debug(f"[translated_df]\n{translated_df}")
            self.translation = translated_df
            self.status = status
        except Exception as e:
            logger.error(f"An error occurred during table translation: {e}")
            self.translation = None
            self.status = False

    def __str__(self):
        return self.original.to_string(header=False, index=False)

    def iter_items(self, translated=False):
        target_df = self.translation if translated else self.original
        for row_idx, row in target_df.iterrows():
            for col_idx, item in enumerate(row):
                yield (row_idx, col_idx, item)

    def update_item(self, row_idx, col_idx, new_value, translated=False):
        target_df = self.translation if translated else self.original
        target_df.at[row_idx, col_idx] = new_value

    def get_original_as_str(self):
        return self.original.to_string(header=False, index=False)