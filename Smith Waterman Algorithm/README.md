Text Similarity Analysis : 

The Smith-Waterman local alignment algorithm is used to find maximal local alignments within two text fragments. This program is used to read, tokenize, and normalize the text in the two files. The program then generates and reports the edit distance and backtrace tables that are used by the algorithm. Finally, the program uses the tables to identify and report all maximal-value alignments that are found in the tables.

Tokenization and Normalization: 

The text in both input files are tokenized and normalized. Tokenization will involve simply splitting the inputs on whitespace. This will produce raw tokens for both source and target. Each raw token is normalized according to the following rules. a) First, all tokens are converted to lower case. b) If a token contains alphanumeric characters and the first character or characters is (or are) non-alphanumeric, then each such leading non-alphanumeric character is split off as a separate token; c) Whether or not the second rule was applied, if the token contains alphanumeric characters and the last character or characters is (or are) non-alphanumeric, then each such trailing non-alphanumeric character is split off as a separate token, which is added in the correct order after application of Rule 4; d) After application of the preceding rules, whichever one of the following applicable sub-rules is applied:

If the token ends with "'s" (apostrophe, followed by the letter s), then it is split into two tokens: the part preceding the apostrophe, and the token "'s";
If the token end with "n't" (n-apostrophe-t), then it is split into two tokens: the part preceding the "n", and the token "not";
If the token end with "'m" (apostrophe-m), then it is split into two tokens: the part preceding the apostrophe, and the token "am"; and
If none of the preceding sub-rules applies, then the token is accepted as it is.

Algorithm Parameters: 

The following parameters are used for the Smith-Waterman local alignment algorithm: a) Gap penalty for insertions and deletions: -1 b) Mismatch penalty of -1 c) and Match score of +2.
