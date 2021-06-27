// Generated from d:\Projetos\project_ccedilha_compiler\ccedilha.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ccedilhaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, WS=3, ENDLINE=4, INT=5, STRING=6, FLOAT=7, BOOL=8, ID=9, 
		LKEY=10, RKEY=11, LPAREN=12, RPAREN=13, EQUAL=14, IF=15, ELSE=16, WHILE=17, 
		AND=18, OR=19, GREATER_EQUAL=20, LESSER_EQUAL=21, GREATER=22, LESSER=23, 
		PLUS=24, MINUS=25, MULT=26, DIV=27, REST=28, PLUS_PLUS=29, MINUS_MINUS=30;
	public static final int
		RULE_prog = 0, RULE_main = 1, RULE_att = 2, RULE_func = 3, RULE_expr = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "main", "att", "func", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'nada principal()'", "'amostrar'", null, null, null, null, null, 
			null, null, "'{'", "'}'", "'('", "')'", "' igual '", "'se'", "'senao'", 
			"'enquanto'", "' e '", "' ou '", "' maiorIgual '", "' menorIgual '", 
			"' maior '", "' menor '", "' mais '", "' menos '", "' vezes '", "' divide '", 
			"' resto '", "' maisMais'", "' menosMenos'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "WS", "ENDLINE", "INT", "STRING", "FLOAT", "BOOL", 
			"ID", "LKEY", "RKEY", "LPAREN", "RPAREN", "EQUAL", "IF", "ELSE", "WHILE", 
			"AND", "OR", "GREATER_EQUAL", "LESSER_EQUAL", "GREATER", "LESSER", "PLUS", 
			"MINUS", "MULT", "DIV", "REST", "PLUS_PLUS", "MINUS_MINUS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ccedilha.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ccedilhaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			main();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public TerminalNode LKEY() { return getToken(ccedilhaParser.LKEY, 0); }
		public TerminalNode RKEY() { return getToken(ccedilhaParser.RKEY, 0); }
		public List<FuncContext> func() {
			return getRuleContexts(FuncContext.class);
		}
		public FuncContext func(int i) {
			return getRuleContext(FuncContext.class,i);
		}
		public List<AttContext> att() {
			return getRuleContexts(AttContext.class);
		}
		public AttContext att(int i) {
			return getRuleContext(AttContext.class,i);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			match(T__0);
			setState(13);
			match(LKEY);
			setState(16); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(16);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(14);
					func();
					}
					break;
				case 2:
					{
					setState(15);
					att();
					}
					break;
				}
				}
				setState(18); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__1 || _la==ID );
			setState(20);
			match(RKEY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AttContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ccedilhaParser.ID, 0); }
		public TerminalNode EQUAL() { return getToken(ccedilhaParser.EQUAL, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ENDLINE() { return getToken(ccedilhaParser.ENDLINE, 0); }
		public AttContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_att; }
	}

	public final AttContext att() throws RecognitionException {
		AttContext _localctx = new AttContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_att);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(ID);
			setState(23);
			match(EQUAL);
			setState(24);
			expr(0);
			setState(25);
			match(ENDLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncContext extends ParserRuleContext {
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	 
		public FuncContext() { }
		public void copyFrom(FuncContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FuncMinusMinusContext extends FuncContext {
		public TerminalNode ID() { return getToken(ccedilhaParser.ID, 0); }
		public TerminalNode MINUS_MINUS() { return getToken(ccedilhaParser.MINUS_MINUS, 0); }
		public TerminalNode ENDLINE() { return getToken(ccedilhaParser.ENDLINE, 0); }
		public FuncMinusMinusContext(FuncContext ctx) { copyFrom(ctx); }
	}
	public static class FuncPlusPlusContext extends FuncContext {
		public TerminalNode ID() { return getToken(ccedilhaParser.ID, 0); }
		public TerminalNode PLUS_PLUS() { return getToken(ccedilhaParser.PLUS_PLUS, 0); }
		public TerminalNode ENDLINE() { return getToken(ccedilhaParser.ENDLINE, 0); }
		public FuncPlusPlusContext(FuncContext ctx) { copyFrom(ctx); }
	}
	public static class FuncPrintContext extends FuncContext {
		public TerminalNode LPAREN() { return getToken(ccedilhaParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ccedilhaParser.RPAREN, 0); }
		public TerminalNode ENDLINE() { return getToken(ccedilhaParser.ENDLINE, 0); }
		public TerminalNode STRING() { return getToken(ccedilhaParser.STRING, 0); }
		public TerminalNode INT() { return getToken(ccedilhaParser.INT, 0); }
		public TerminalNode ID() { return getToken(ccedilhaParser.ID, 0); }
		public FuncPrintContext(FuncContext ctx) { copyFrom(ctx); }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_func);
		int _la;
		try {
			setState(38);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new FuncPrintContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(27);
				match(T__1);
				setState(28);
				match(LPAREN);
				setState(29);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << STRING) | (1L << ID))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(30);
				match(RPAREN);
				setState(31);
				match(ENDLINE);
				}
				break;
			case 2:
				_localctx = new FuncPlusPlusContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(32);
				match(ID);
				setState(33);
				match(PLUS_PLUS);
				setState(34);
				match(ENDLINE);
				}
				break;
			case 3:
				_localctx = new FuncMinusMinusContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(35);
				match(ID);
				setState(36);
				match(MINUS_MINUS);
				setState(37);
				match(ENDLINE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExprMultDivContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MULT() { return getToken(ccedilhaParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(ccedilhaParser.DIV, 0); }
		public ExprMultDivContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ExprParenContext extends ExprContext {
		public TerminalNode LPAREN() { return getToken(ccedilhaParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ccedilhaParser.RPAREN, 0); }
		public ExprParenContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ExprPlusMinusContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(ccedilhaParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(ccedilhaParser.MINUS, 0); }
		public ExprPlusMinusContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NumberContext extends ExprContext {
		public TerminalNode INT() { return getToken(ccedilhaParser.INT, 0); }
		public NumberContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(ccedilhaParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				_localctx = new NumberContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(41);
				match(INT);
				}
				break;
			case ID:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(42);
				match(ID);
				}
				break;
			case LPAREN:
				{
				_localctx = new ExprParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(43);
				match(LPAREN);
				setState(44);
				expr(0);
				setState(45);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(57);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(55);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ExprMultDivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(49);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(50);
						_la = _input.LA(1);
						if ( !(_la==MULT || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(51);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprPlusMinusContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(52);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(53);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(54);
						expr(5);
						}
						break;
					}
					} 
				}
				setState(59);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ?\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3\3\3\3\3\3\3\6\3\23\n\3\r\3\16\3\24"+
		"\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\5\5)\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\62\n\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\7\6:\n\6\f\6\16\6=\13\6\3\6\2\3\n\7\2\4\6\b\n\2\5\4\2\7\b\13\13\3"+
		"\2\34\35\3\2\32\33\2A\2\f\3\2\2\2\4\16\3\2\2\2\6\30\3\2\2\2\b(\3\2\2\2"+
		"\n\61\3\2\2\2\f\r\5\4\3\2\r\3\3\2\2\2\16\17\7\3\2\2\17\22\7\f\2\2\20\23"+
		"\5\b\5\2\21\23\5\6\4\2\22\20\3\2\2\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22"+
		"\3\2\2\2\24\25\3\2\2\2\25\26\3\2\2\2\26\27\7\r\2\2\27\5\3\2\2\2\30\31"+
		"\7\13\2\2\31\32\7\20\2\2\32\33\5\n\6\2\33\34\7\6\2\2\34\7\3\2\2\2\35\36"+
		"\7\4\2\2\36\37\7\16\2\2\37 \t\2\2\2 !\7\17\2\2!)\7\6\2\2\"#\7\13\2\2#"+
		"$\7\37\2\2$)\7\6\2\2%&\7\13\2\2&\'\7 \2\2\')\7\6\2\2(\35\3\2\2\2(\"\3"+
		"\2\2\2(%\3\2\2\2)\t\3\2\2\2*+\b\6\1\2+\62\7\7\2\2,\62\7\13\2\2-.\7\16"+
		"\2\2./\5\n\6\2/\60\7\17\2\2\60\62\3\2\2\2\61*\3\2\2\2\61,\3\2\2\2\61-"+
		"\3\2\2\2\62;\3\2\2\2\63\64\f\7\2\2\64\65\t\3\2\2\65:\5\n\6\b\66\67\f\6"+
		"\2\2\678\t\4\2\28:\5\n\6\79\63\3\2\2\29\66\3\2\2\2:=\3\2\2\2;9\3\2\2\2"+
		";<\3\2\2\2<\13\3\2\2\2=;\3\2\2\2\b\22\24(\619;";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}