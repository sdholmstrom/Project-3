# Project-3: TradeSmart Analyzer
## The Idea: Blend Fundamental and Technical Analysis Techniques to Identify and Guide Invement Opportunities
Fundamental Analysis measures a security's intrinsic value by examining related economic and financial factors. Intrinsic value is the value of an investment based on the issuing company's financial situation and current market and economic conditions.

Technical Analysis is a trading discipline employed to evaluate investments and identify trading opportunities by analyzing statistical trends gathered from trading activity, such as price movement and volume. Unlike fundamental analysis, which attempts to evaluate a security's value based on business results such as sales and earnings, technical analysis focuses on the study of price and volume.

By utilizing these two methods we can identify a healthy investment opportunity AND when the ideal time is to jump in or jump out.

## Instructions:
Intrinsic Value Calculation:
1. Load imports and ensure your .env file has a valid API key. The Financial Modeling Prep api requires a paid subscription for access to quarterly financial data that is used within our model.
2. Update the ticker object in cell 2.
3. Run all cells and view the output components (Intrinsic Value, Current Share Price, and Margin of Safety) to see if your selected stock is over or undervalued.

Technical Anlaysis (Simple Moving Averages):
1.


## Analysis Summary:
The component pieces of our application work as designed; the DCF model produces a margin of over or undervalue of a specific stock. The limitations of the DCF model are evident when looking at growth companies or those that have recently exoerienced changes in FCF trends. Apple which has a strong FCF performance produces a seemingly close intrinsic value, while showing it is slightly overvalued by the market right now (8% overvalued).
![AAPLIntrinsicValue](README%20Visuals/AAPL%20Intrinsic%20Value.png)

Target, having recently experienced some negative FCF quarters produces a much lower intrinsic value and would suggest it is nowhere close to being worthy of purchase. If the investor has a postiion in TGT, they would do well to get out right now.
![TGTIntrinsicValue](README%20Visuals/TGT%20Intrinsic%20Value.png)

At least part of the limitations of this particular DCF model can be explained by the influential assumptions made around FCF projections, growth rates, and discount rate. Each of these components would be better served in a later iteration to be modeled out individually and in a more thorough approach.

Technical Analysis notes here...
