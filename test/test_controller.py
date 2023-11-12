# def test_can_you_start_the_quiz_more_than_once_per_day():
#     controller = Controller()
#     # Check if it's the first quiz of the day
#     first_attempt = controller.first_quiz_today()
#     assert first_attempt is True  # It should be the first attempt on the same day
#
#     # Start the quiz
#     # controller.quiz()
#     controller.model.save_quiz_date()
#
#     # Check if it's the first quiz of the day again
#     second_attempt = controller.first_quiz_today()
#     assert second_attempt is False  # It should be the second attempt on the same day

# @patch('builtins.open', new_callable=mock_open)
# def test_can_you_start_the_quiz_more_than_once_per_day(mock_file):
#     today = str(datetime.today()).split(" ")[0]
#     # Create a temporary file for the quiz date
#     temp_quiz_date = {"data": "2023-10-28"}  # Set the desired date
#     file_path = 'temp_quiz_date.json'
#     with open(file_path, 'w', encoding="utf-8") as temp_file:
#         json.dump(temp_quiz_date, temp_file)
#     print(f"File path: {file_path}")
#
#     controller = Controller()
#
#     # Check if it's the first quiz of the day
#     first_attempt = controller.first_quiz_today()
#     assert first_attempt is True  # It should be the first attempt on the same day
#
#     # Start the quiz
#     # controller.quiz()
#     controller.model.save_quiz_date('temp_quiz_date.json')
#
#     # Check if it's the first quiz of the day again
#     second_attempt = controller.first_quiz_today()
#     assert second_attempt is False  # It should be the second attempt on the same day
#
#     # Clean up the temporary file
#     temp_file.close()

# @patch('builtins.open', new_callable=mock_open)
# def test_can_you_start_the_quiz_more_than_once_per_day(mock_file):
#     # Set the desired date
#     temp_quiz_date = {"data": "2023-10-28"}
#     mock_file.return_value.read.return_value = json.dumps(temp_quiz_date)
#
#     controller = Controller()
#
#     # Check if it's the first quiz of the day
#     first_attempt = controller.first_quiz_today()
#     assert first_attempt is True  # It should be the first attempt on the same day
#
#     # Mock the file writing operation to do nothing
#     with patch('builtins.open', new_callable=mock_open) as mock_write:
#         controller.model.save_quiz_date('temp_quiz_date.json')
#
#     # Check if it's the first quiz of the day again
#     second_attempt = controller.first_quiz_today()
#     assert second_attempt is False  # It should be the second attempt on the same day



