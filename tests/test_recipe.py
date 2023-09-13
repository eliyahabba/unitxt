import unittest

from src.unitxt.formats import ICLFormat
from src.unitxt.instructions import TextualInstruction
from src.unitxt.standard import StandardRecipe
from src.unitxt.templates import InputOutputTemplate
from src.unitxt.text_utils import print_dict


class TestRecipes(unittest.TestCase):
    def test_standard_recipe(self):
        recipe = StandardRecipe(
            card="cards.wnli",
            instruction=TextualInstruction(text="classify"),
            template=InputOutputTemplate(
                input_format="{premise}",
                output_format="{label}",
            ),
            format=ICLFormat(
                input_prefix="User:",
                output_prefix="Agent:",
            ),
        )
        stream = recipe()

        for instance in stream["train"]:
            print_dict(instance)
            break

    def test_standard_recipe_with_catalog(self):
        recipe = StandardRecipe(
            card="cards.mmlu.marketing",
            instruction="instructions.models.llama",
            template="templates.mmlu.lm_eval_harness",
            format="formats.user_agent",
            demos_pool_size=100,
            num_demos=3,
        )

        stream = recipe()

        for instance in stream["train"]:
            print_dict(instance)
            break