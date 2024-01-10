ranking_prompt = """
Given these questions and answers between === START QUESTION_ANSWER === and === END QUENSTION_ANSWER ===, 
can you please re-rank the questions (from most relevant to most irrelevant) you can find between === START RANKING_QUESTIONS === and === END RANKING_QUESTIONS === in terms of prominence to assess this topic: "Business Strategy"?

=== START QUESTION_ANSWER ===
Is there a published business strategy that data strategy needs to align to?

Yes, we have a very detailed published business strategy.
=== END QUENSTION_ANSWER ===

=== START RANKING_QUESTIONS ===
Does your current data strategy align with your business strategy? Are there gaps or misalignments to address?
Is there market demand for the type of data your organization possess?
Are there any known GenAI use cases or would the orgranization be interested in knowing how data strategy can be enabler for GenAI?
Are you aware of the potential business impact of analyzing and using currently untapped data sources?
Is there data governance that aligns and support business objectives?
Do you have executive support for data initiatives?
Is there budget allocated for data infrastructure needs?
Have you explored various monetization models (e.g., data licensing, data subscriptions, data-as-a-service)?
Is there a need or opportunity to simplify data sharing and collaboration amoungst internal teams?
Is there a need to democratize data access and empower business units or teams to access and analyze data independently?
Are there emerging use cases that require agility in data access and processing?
Are there bottlenecks in data access, processing, or analytics?
How long does it take for a medium size complexity analytical project to from requirements to production? Are there any concerns about the time it takes to go live?
Does your organization have the necessary skills in-house, or do you rely on external expertise?
=== END RANKING_QUESTIONS ===

The model will then use the provided answers to the questions to generate a ranked list of questions that are most relevant to the topic of Business Strategy. The ranked list will be provided in the output of the model.
Can you please respond using a JSON list with the topics like this one:
```json
[
"Is there market demand for the type of data your organization possess?",
"Is there a need or opportunity to simplify data sharing and collaboration amoungst internal teams?"
]
```
"""
