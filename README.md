# candidate-sentiment-api
API Server to parse and retrieve tweet sentiments for political candidates 

## Methodology
Using a sentiment-parsing library, the following are aggregated for each candidate:
- Replies to candidate's tweets
- Tweets with one of the 5 most popular hashtags associated with the candidate
- Tweets referencing candidate's account
- Tweets mentioning the candidate by name

A stream of the past 24 hours worth of data, chunked by novel tweets in 10 minute intervals, is maintained

## License
The MIT License (MIT)

Copyright (c) 2016 Jimmy Gong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.