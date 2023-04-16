# Backseat Driver: GitHub Action

Requests a code review from a large language model.
See the [Backseat Driver repository](https://github.com/kostaleonard/backseat-driver)
for more details.

## Usage

### Arguments

|Argument|Required| Description                                                                                                          |
|---|---|----------------------------------------------------------------------------------------------------------------------|
|openai-api-key|true|The user's OpenAI API key.|
|filenames|true|The files to pass to the LLM for code review as a space-separated list. Each value can be a file or a blob-style path.|
|fail-under|false|If specified, exit with non-zero status if the LLM's grade falls below the given value. The value should be one of {'A', 'B', 'C', 'D'}. This value is not inclusive: if this value is 'B' and the LLM gives a final grade of 'B,' then the program will exit with a zero status. If not specified, then the program will exit with a zero status no matter the LLM's grade.|

### Example

```yaml
uses: actions/backseat-driver-action@v1
with:
  openai-api-key: ${{ secrets.OPENAI_API_KEY }}
  filenames: '**/*.py'
  fail-under: B
```
