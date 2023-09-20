#-*-coding: gbk-*-
import unittest
import tempfile
from main import *

class TestPaperSimilarity(unittest.TestCase):
    def test_remove_punctuation(self):
        # ����ȥ�������ŵĺ���
        text_with_punctuation = "�������������     �ģ���ģ���  ��. ����!"
        expected_result = "����������������ĺð�����"
        result = remove_punctuation(text_with_punctuation)
        self.assertEqual(result, expected_result)

    def test_calculate_similarity(self):
        # ���Լ��������Եĺ���
        original_text = "������֣����ڲ��ԡ��������Ҳ���ڲ���,�������Ҳ���ڲ���,�������Ҳ���ڲ���"
        text_to_check = "�������, ���ڲ��ԡ��������Ҳ���ڲ���,�������Ҳ���ڲ���,�������Ҳ���ڲ���"
        expected_similarity = 1  # ʾ��ֵ
        similarity = calculate_similarity(original_text, text_to_check)
        self.assertAlmostEqual(similarity, expected_similarity, places=2)  # ���������ֵ�Ƿ�ӽ�����ֵ

    def test_read_file(self):
            # ������ʱ�ļ���ģ�������ļ�
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(b"Hello, World!")
                file_content = read_file(temp_file.name)

                # �����ļ�������ȷ
                self.assertEqual(file_content, "Hello, World!")

            # ������ʱ�ļ��ѱ�ɾ��
            self.assertFalse(os.path.exists(temp_file.name))

    def test_read_nonexistent_file(self):
        # ���Զ�ȡ�����ڵ��ļ��Ƿ������쳣
        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent.txt")

    def test_tokenize_chinese_text(self):
        # �������ķִʵĺ���
        chinese_text = "����������ú��ʺ�ȥ����"
        expected_result = "�������� ��� �� �ʺ� ȥ ����"
        result = tokenize_chinese_text(chinese_text)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

