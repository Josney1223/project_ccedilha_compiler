// Generated from d:\Projetos\project_ccedilha_compiler\ccedilha.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ccedilhaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, WS=3, ENDLINE=4, INT=5, STRING=6, FLOAT=7, BOOL=8, ID=9, 
		LKEY=10, RKEY=11, LPAREN=12, RPAREN=13, EQUAL=14, IF=15, ELSE=16, WHILE=17, 
		AND=18, OR=19, GREATER_EQUAL=20, LESSER_EQUAL=21, GREATER=22, LESSER=23, 
		PLUS=24, MINUS=25, MULT=26, DIV=27, REST=28, PLUS_PLUS=29, MINUS_MINUS=30;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "WS", "SINAL", "ENDLINE", "INT", "STRING", "FLOAT", "BOOL", 
			"ID", "LKEY", "RKEY", "LPAREN", "RPAREN", "EQUAL", "IF", "ELSE", "WHILE", 
			"AND", "OR", "GREATER_EQUAL", "LESSER_EQUAL", "GREATER", "LESSER", "PLUS", 
			"MINUS", "MULT", "DIV", "REST", "PLUS_PLUS", "MINUS_MINUS"
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


	public ccedilhaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ccedilha.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 \u012a\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\6\4]\n\4\r\4\16\4^\3\4\3\4\3\5\3\5"+
		"\3\6\3\6\3\7\5\7h\n\7\3\7\6\7k\n\7\r\7\16\7l\3\b\3\b\6\bq\n\b\r\b\16\b"+
		"r\3\b\3\b\3\t\6\tx\n\t\r\t\16\ty\3\t\3\t\6\t~\n\t\r\t\16\t\177\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0091\n\n\3\13"+
		"\6\13\u0094\n\13\r\13\16\13\u0095\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24"+
		"\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34"+
		"\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37"+
		"\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \2\2!\3\3\5\4\7\5\t\2\13\6\r"+
		"\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20!\21#\22%\23\'\24)"+
		"\25+\26-\27/\30\61\31\63\32\65\33\67\349\35;\36=\37? \3\2\b\5\2\13\f\17"+
		"\17\"\"\4\2--//\3\2\u00e9\u00e9\3\2\62;\4\2^^pp\4\2C\\c|\2\u0130\2\3\3"+
		"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2"+
		"\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3"+
		"\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'"+
		"\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63"+
		"\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2"+
		"?\3\2\2\2\3A\3\2\2\2\5R\3\2\2\2\7\\\3\2\2\2\tb\3\2\2\2\13d\3\2\2\2\rg"+
		"\3\2\2\2\17n\3\2\2\2\21w\3\2\2\2\23\u0090\3\2\2\2\25\u0093\3\2\2\2\27"+
		"\u0097\3\2\2\2\31\u0099\3\2\2\2\33\u009b\3\2\2\2\35\u009d\3\2\2\2\37\u009f"+
		"\3\2\2\2!\u00a7\3\2\2\2#\u00aa\3\2\2\2%\u00b0\3\2\2\2\'\u00b9\3\2\2\2"+
		")\u00bd\3\2\2\2+\u00c2\3\2\2\2-\u00cf\3\2\2\2/\u00dc\3\2\2\2\61\u00e4"+
		"\3\2\2\2\63\u00ec\3\2\2\2\65\u00f3\3\2\2\2\67\u00fb\3\2\2\29\u0103\3\2"+
		"\2\2;\u010c\3\2\2\2=\u0114\3\2\2\2?\u011e\3\2\2\2AB\7p\2\2BC\7c\2\2CD"+
		"\7f\2\2DE\7c\2\2EF\7\"\2\2FG\7r\2\2GH\7t\2\2HI\7k\2\2IJ\7p\2\2JK\7e\2"+
		"\2KL\7k\2\2LM\7r\2\2MN\7c\2\2NO\7n\2\2OP\7*\2\2PQ\7+\2\2Q\4\3\2\2\2RS"+
		"\7c\2\2ST\7o\2\2TU\7q\2\2UV\7u\2\2VW\7v\2\2WX\7t\2\2XY\7c\2\2YZ\7t\2\2"+
		"Z\6\3\2\2\2[]\t\2\2\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_`\3\2"+
		"\2\2`a\b\4\2\2a\b\3\2\2\2bc\t\3\2\2c\n\3\2\2\2de\t\4\2\2e\f\3\2\2\2fh"+
		"\5\t\5\2gf\3\2\2\2gh\3\2\2\2hj\3\2\2\2ik\t\5\2\2ji\3\2\2\2kl\3\2\2\2l"+
		"j\3\2\2\2lm\3\2\2\2m\16\3\2\2\2np\7$\2\2oq\n\6\2\2po\3\2\2\2qr\3\2\2\2"+
		"rp\3\2\2\2rs\3\2\2\2st\3\2\2\2tu\7$\2\2u\20\3\2\2\2vx\t\5\2\2wv\3\2\2"+
		"\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z{\3\2\2\2{}\7\60\2\2|~\t\5\2\2}|\3\2"+
		"\2\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\22\3\2\2\2\u0081"+
		"\u0082\7x\2\2\u0082\u0083\7g\2\2\u0083\u0084\7t\2\2\u0084\u0085\7f\2\2"+
		"\u0085\u0086\7c\2\2\u0086\u0087\7f\2\2\u0087\u0088\7g\2\2\u0088\u0089"+
		"\7k\2\2\u0089\u008a\7t\2\2\u008a\u0091\7q\2\2\u008b\u008c\7h\2\2\u008c"+
		"\u008d\7c\2\2\u008d\u008e\7n\2\2\u008e\u008f\7u\2\2\u008f\u0091\7q\2\2"+
		"\u0090\u0081\3\2\2\2\u0090\u008b\3\2\2\2\u0091\24\3\2\2\2\u0092\u0094"+
		"\t\7\2\2\u0093\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2\u0095"+
		"\u0096\3\2\2\2\u0096\26\3\2\2\2\u0097\u0098\7}\2\2\u0098\30\3\2\2\2\u0099"+
		"\u009a\7\177\2\2\u009a\32\3\2\2\2\u009b\u009c\7*\2\2\u009c\34\3\2\2\2"+
		"\u009d\u009e\7+\2\2\u009e\36\3\2\2\2\u009f\u00a0\7\"\2\2\u00a0\u00a1\7"+
		"k\2\2\u00a1\u00a2\7i\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5"+
		"\7n\2\2\u00a5\u00a6\7\"\2\2\u00a6 \3\2\2\2\u00a7\u00a8\7u\2\2\u00a8\u00a9"+
		"\7g\2\2\u00a9\"\3\2\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad"+
		"\7p\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af\7q\2\2\u00af$\3\2\2\2\u00b0\u00b1"+
		"\7g\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7s\2\2\u00b3\u00b4\7w\2\2\u00b4"+
		"\u00b5\7c\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7q\2\2"+
		"\u00b8&\3\2\2\2\u00b9\u00ba\7\"\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7\""+
		"\2\2\u00bc(\3\2\2\2\u00bd\u00be\7\"\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0"+
		"\7w\2\2\u00c0\u00c1\7\"\2\2\u00c1*\3\2\2\2\u00c2\u00c3\7\"\2\2\u00c3\u00c4"+
		"\7o\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7q\2\2\u00c7"+
		"\u00c8\7t\2\2\u00c8\u00c9\7K\2\2\u00c9\u00ca\7i\2\2\u00ca\u00cb\7w\2\2"+
		"\u00cb\u00cc\7c\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce\7\"\2\2\u00ce,\3\2"+
		"\2\2\u00cf\u00d0\7\"\2\2\u00d0\u00d1\7o\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3"+
		"\7p\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7K\2\2\u00d6"+
		"\u00d7\7i\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7n\2\2"+
		"\u00da\u00db\7\"\2\2\u00db.\3\2\2\2\u00dc\u00dd\7\"\2\2\u00dd\u00de\7"+
		"o\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2"+
		"\7t\2\2\u00e2\u00e3\7\"\2\2\u00e3\60\3\2\2\2\u00e4\u00e5\7\"\2\2\u00e5"+
		"\u00e6\7o\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7q\2\2"+
		"\u00e9\u00ea\7t\2\2\u00ea\u00eb\7\"\2\2\u00eb\62\3\2\2\2\u00ec\u00ed\7"+
		"\"\2\2\u00ed\u00ee\7o\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0\7k\2\2\u00f0"+
		"\u00f1\7u\2\2\u00f1\u00f2\7\"\2\2\u00f2\64\3\2\2\2\u00f3\u00f4\7\"\2\2"+
		"\u00f4\u00f5\7o\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8"+
		"\7q\2\2\u00f8\u00f9\7u\2\2\u00f9\u00fa\7\"\2\2\u00fa\66\3\2\2\2\u00fb"+
		"\u00fc\7\"\2\2\u00fc\u00fd\7x\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7|\2"+
		"\2\u00ff\u0100\7g\2\2\u0100\u0101\7u\2\2\u0101\u0102\7\"\2\2\u01028\3"+
		"\2\2\2\u0103\u0104\7\"\2\2\u0104\u0105\7f\2\2\u0105\u0106\7k\2\2\u0106"+
		"\u0107\7x\2\2\u0107\u0108\7k\2\2\u0108\u0109\7f\2\2\u0109\u010a\7g\2\2"+
		"\u010a\u010b\7\"\2\2\u010b:\3\2\2\2\u010c\u010d\7\"\2\2\u010d\u010e\7"+
		"t\2\2\u010e\u010f\7g\2\2\u010f\u0110\7u\2\2\u0110\u0111\7v\2\2\u0111\u0112"+
		"\7q\2\2\u0112\u0113\7\"\2\2\u0113<\3\2\2\2\u0114\u0115\7\"\2\2\u0115\u0116"+
		"\7o\2\2\u0116\u0117\7c\2\2\u0117\u0118\7k\2\2\u0118\u0119\7u\2\2\u0119"+
		"\u011a\7O\2\2\u011a\u011b\7c\2\2\u011b\u011c\7k\2\2\u011c\u011d\7u\2\2"+
		"\u011d>\3\2\2\2\u011e\u011f\7\"\2\2\u011f\u0120\7o\2\2\u0120\u0121\7g"+
		"\2\2\u0121\u0122\7p\2\2\u0122\u0123\7q\2\2\u0123\u0124\7u\2\2\u0124\u0125"+
		"\7O\2\2\u0125\u0126\7g\2\2\u0126\u0127\7p\2\2\u0127\u0128\7q\2\2\u0128"+
		"\u0129\7u\2\2\u0129@\3\2\2\2\13\2^glry\177\u0090\u0095\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}