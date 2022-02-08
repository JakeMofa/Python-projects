Hello world!
Here is your portfolio:<br/>
  GOOG: <span id=_IG_SYM1_l></span> (<span id=_IG_SYM1_c></span>)<br/>
  AAPL: <span id=_IG_SYM2_l></span> (<span id=_IG_SYM2_c></span>)<br/>
  INTC: <span id=_IG_SYM3_l></span> (<span id=_IG_SYM3_c></span>)<br/>

  
<script type="text/javascript">
  var quote = new google.finance.Quote();
  quote.enableDomUpdates( { 'GOOG' : '_IG_SYM1', 'AAPL' : '_IG_SYM2', 
    'INTC' : '_IG_SYM3' } );

  quote.getQuotes(["GOOG", "AAPL", "INTC"]);
</script>