"""
Operators configuration file.
Stores operator IDs and their corresponding nicknames.
Format: {operator_id: "operator_name"}
"""

# Dictionary mapping operator Telegram IDs to their names
OPERATORS = {
    7968501682: "Едуард Пуля",
    7747809152: "Кавалерка Лайт"
    # Add more operators in the format:
    # 123456789: "Ім'я Оператора",
}

# List of operator IDs (for easier iteration)
OPERATOR_IDS = list(OPERATORS.keys())
