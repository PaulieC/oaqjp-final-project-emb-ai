from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        DOM_EMOTE = 'dominant_emotion'

        # Test case for Dominant Emotion: joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1[DOM_EMOTE], 'joy')

        # Test case for Dominant Emotion: anger
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1[DOM_EMOTE], 'anger')

        # Test case for Dominant Emotion: disgust
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1[DOM_EMOTE], 'disgust')

        # Test case for Dominant Emotion: sadness
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1[DOM_EMOTE], 'sadness')

        # Test case for Dominant Emotion: fear
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1[DOM_EMOTE], 'fear')

unittest.main()