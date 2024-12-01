# LLM Tutorial - Checking grounding prompts

Using the example from Anthropic's [Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial),
I tested the effectiveness of different prompts for avoiding hallucinations.

There are two variables we tested:
1. Whether the prompt includes a request to pull a quote from the document.
2. The order of the document in the prompt.

The results are in `llm_results.txt`.

## Experiment Setup

The question is: `From December 2018 to December 2022, by what amount did Matterport's subscribers grow?`

Relevant quotes from the document:
  - Relative growth: `Our subscribers have grown approximately 49-fold from December 31, 2018 to December 31, 2022.`
  - Absolute number: `As of December 31, 2022, our subscriber base had grown approximately 39% to over 701,000 subscribers from 503,000 subscribers as of December 31, 2021, with our digital twins reaching more than 170 countries.`

We can therefore calculate the absolute growth:
  - Since it grew 49-fold and ended at 701,000, the December 2018 number would have been approximately 701,000 ÷ 49 ≈ 14,306 subscribers.
  - Therefore, Matterport's subscriber base grew by approximately 686,694 subscribers (from ~14,306 to 701,000) during this period.

## Note on Answer Expectations

### Original Success Metric
The original tutorial considers "49-fold growth" as the complete correct answer. By this metric:

- **Anthropic Claude**: 12/12 correct responses
  - All variants provided the 49-fold growth figure
  - Example: `"Matterport's subscribers grew approximately 49-fold (or 4,900%) from December 2018 to December 2022."`

- **OpenAI GPT**: 12/12 correct responses
  - Consistently provided the 49-fold growth across all variants
  - Example: `"Approximately 49 times (or 4,900%) growth in subscribers from December 2018 to December 2022."`

- **Gemini**: 9/12 correct responses
  - Provided 49-fold in nine variants
  - Three anomalous responses giving only an absolute number (698000)

By the original metric, all models performed strongly, with 33/36 responses correctly identifying the 49-fold growth.

### Current Expectations
However, modern LLM capabilities have raised expectations for more comprehensive responses. A more complete answer would:
1. State the relative growth (49-fold)
2. Calculate and provide absolute numbers (from ~14,300 to 701,000)
3. Show the total increase (~686,700 subscribers)

This expanded expectation reveals more significant differences between models and prompt strategies, as detailed in the results below.

## Results

### Test Setup
The experiment tested three LLM models (Anthropic, Gemini, and OpenAI) with four different prompt configurations, running each configuration 3 times:
1. quote_doc_first: Request for quotes + document first
2. quote_doc_second: Request for quotes + document second
3. no_quote_doc_first: No quote request + document first
4. no_quote_doc_second: No quote request + document second

### Performance by Model

**Anthropic Claude** showed consistent performance across iterations:
- All 12 responses (4 variants × 3 iterations) were accurate
- Document-second variants consistently provided the most comprehensive answers
- Quote-based prompts tended to produce more detailed explanations
- Responses were stable across iterations, showing no variance in accuracy

Example responses across iterations (document-second):
```
Iteration 1: "Matterport's subscribers grew from approximately 14,300 (701,000 ÷ 49) in December 2018 to 701,000 in December 2022, which represents a growth of approximately 686,700 subscribers."

Iteration 2: "From December 2018 to December 2022, Matterport's subscribers grew approximately 49-fold, from a base of around 14,300 subscribers (701,000 ÷ 49) to over 701,000 subscribers."

Iteration 3: "From December 2018 to December 2022, Matterport's subscribers grew approximately 49-fold, from around 14,300 subscribers to over 701,000 subscribers."
```

**OpenAI GPT** showed high consistency but less detail:
- All 12 responses correctly identified the 49-fold growth
- Responses were remarkably consistent across iterations
- Did not perform additional calculations in any iteration
- Format and wording remained nearly identical across runs

Example responses across iterations:
```
Iteration 1: "Approximately 49 times (49-fold) growth in subscribers."
Iteration 2: "Approximately 49 times (or 4,900%) from December 2018 to December 2022."
Iteration 3: "49-fold increase in subscribers"
```

**Gemini** showed the most variability:
- Responses were consistent within iterations but showed concerning patterns
- All no_quote_doc_second variants gave the same incorrect absolute number (698,000)
- Quote-based responses showed unnecessary hedging in all iterations
- Performance did not improve across iterations

Example of consistent hedging across iterations:
```
Iteration 1: "The provided text states a 49-fold increase, but does not provide the specific numerical subscriber count..."
Iteration 2: "The provided text states a 49-fold increase, but does not provide the specific numerical subscriber count..."
Iteration 3: "The provided text states a 49-fold increase but does not provide the specific numbers..."
```

### Performance by Prompt Variant

**Document Placement**:
- Document-first prompts consistently produced more reliable results across all models
- Gemini performed notably better with document-first variants
- Claude provided more detailed calculations with document-second, but remained accurate with either placement
- OpenAI maintained consistent performance regardless of placement

**Quote Request**:
- The presence of a quote request had less impact than document placement
- Quote requests helped prevent hallucination in Gemini's document-second variants
- Quote requests led to more detailed explanations in Claude's responses
- OpenAI's responses remained consistent regardless of quote requests

### Key Takeaways
- Document-first placement generally produced more reliable results across models.
- Quote requests had a secondary but positive effect, particularly in preventing hallucinations and encouraging more detailed explanations.