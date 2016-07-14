# EODP: Exploring Open Data Policies

The goal of this project is to parse open data policies, laws, and executive orders in order to extract useful information from them.


## Understanding document structure

We can think about the structure of open data policies in two ways: by ordered parts or by functional components. 

### Ordered parts/sections

Every open data law, executive order, or policy has some combination of several basic parts. These parts are:
- **Front matter:** This is the text at the very top.
- **Preamble:** For now, this will be defined specifically as a series of "WHEREAS" clauses, typically stating the reasons for adopting the open data policy.
- **Transition:** Often one or two lines, this signals a transition from the front matter or preamble to the main body. For now, this needs to have one of the words "therefore," "hereby," or "ordained," with a colon at the end of the sentence.
- **Main body:** This is usually where most of the text is.
- **Conclusion:** This signals the end of the bill or order. 
- **Appendix:** Sometimes, there will be policy details listed at the end instead of in the main body.

Most don't have *all* of these parts, but the ones they do have alre always *in this order*. At the very least, nearly every document will have front matter and a main body.

### Functional components

The actual content of these ordered parts varies widely, so there's a separate dimension to consider: functional components. These are specific functional units of the law/order/policy, and they may be found in any of the parts listed above, though most tend to be found in only a subset of the above parts. (One document may have multiple of these components found in one part of the document, and one component may be spread across several of the ordered parts.) The components are:

- **Metadata:** Typically found in the *front matter*, *transition*, and *conclusion*, this includes:
	- Official name of the local government
	- Date passed or ordered
	- Date effective
	- Bill or executive order number
	- Bill, executive order, or policy name
	- Name of the mayor or city manager (found in nearly all executive orders, plus some laws and policies)
- **Justification:** Typically found in the *preamble* or *main body*, this is a statement or series of statements explaining the reason for the law/order/policy.
- **Summary:** Typically found in the *front matter*, *preamble*, *transition*, or *main body*, this is a summary of the law/order/policy. Not all documents contain this.
- **Definitions:** Typically found in the *preamble*, *main body*, or *appendix*, this is a list of terms and their definitions. Not all documents contain this.
- **Policy details:** Typically found in the *main body* or *appendix*, this is the real substance of the policy, laying out its details. It includes some combination of items like:
	- The name of which government department or office is in charge of executing the policy
	- The name and description of a specific relevant position, such as a Chief Data Officer, Chief Information Officer, Chief Technology Officer, or Open Data Manager
	- The name and description of a relevant new committee or working group
	- Requirements for each city department to follow
	- The URL of the open data website
	- Information on what formats the data should be in (like a requirement for machine-readability)
	- A list of datasets that must be included or should be prioritized
	- Policy evaluation criteria and reporting requirements
	- A suggestion for the policy to be reviewed in the future
	- A legal disclaimer on data quality

So if different documents have these pieces of information arraged in very different ways, why do we care about the structured parts? Because picking these policies apart to find different functional components is hard, so we can use information about what parts of the document they are likely to be found in to help us find them.
