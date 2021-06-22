// Generated from d:\Projetos\project_ccedilha_compiler\ccedilhaTokens.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ccedilhaTokens extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ENDLINE=1, INT=2, STRING=3, FLOAT=4, BOOL=5, ID=6, LKEY=7, RKEY=8, LPAREN=9, 
		RPAREN=10, EQUAL=11, IF=12, ELSE=13, WHILE=14, AND=15, OR=16, GREATER_EQUAL=17, 
		LESSER_EQUAL=18, GREATER=19, LESSER=20, PLUS=21, MINUS=22, MULT=23, DIV=24, 
		REST=25, PLUS_PLUS=26, MINUS_MINUS=27, WS=28;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SINAL", "ENDLINE", "INT", "STRING", "FLOAT", "BOOL", "ID", "LKEY", "RKEY", 
			"LPAREN", "RPAREN", "EQUAL", "IF", "ELSE", "WHILE", "AND", "OR", "GREATER_EQUAL", 
			"LESSER_EQUAL", "GREATER", "LESSER", "PLUS", "MINUS", "MULT", "DIV", 
			"REST", "PLUS_PLUS", "MINUS_MINUS", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, "'{'", "'}'", "'('", "')'", 
			"' igual '", "'se'", "'senao'", "'enquanto'", "' e '", "' ou '", "' maiorIgual '", 
			"' menorIgual '", "' maior '", "' menor '", "' mais '", "' menos '", 
			"' vezes '", "' divide '", "' resto '", "' maisMais'", "' menosMenos'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ENDLINE", "INT", "STRING", "FLOAT", "BOOL", "ID", "LKEY", "RKEY", 
			"LPAREN", "RPAREN", "EQUAL", "IF", "ELSE", "WHILE", "AND", "OR", "GREATER_EQUAL", 
			"LESSER_EQUAL", "GREATER", "LESSER", "PLUS", "MINUS", "MULT", "DIV", 
			"REST", "PLUS_PLUS", "MINUS_MINUS", "WS"
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


	public ccedilhaTokens(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ccedilhaTokens.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36\u010c\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\3\2\3\2\3\3\3"+
		"\3\3\4\5\4C\n\4\3\4\6\4F\n\4\r\4\16\4G\3\5\3\5\6\5L\n\5\r\5\16\5M\3\5"+
		"\3\5\3\6\6\6S\n\6\r\6\16\6T\3\6\3\6\6\6Y\n\6\r\6\16\6Z\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7l\n\7\3\b\6\bo\n\b\r\b"+
		"\16\bp\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3"+
		"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3"+
		"\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3"+
		"\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3"+
		"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3"+
		"\35\3\35\3\35\3\35\3\35\3\35\3\36\6\36\u0107\n\36\r\36\16\36\u0108\3\36"+
		"\3\36\2\2\37\3\2\5\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33"+
		"\16\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67"+
		"\349\35;\36\3\2\b\4\2--//\3\2\u00e9\u00e9\3\2\62;\4\2^^pp\4\2C\\c|\5\2"+
		"\13\f\17\17\"\"\2\u0112\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2"+
		"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2"+
		"\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2"+
		"\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2"+
		"\2\2\2;\3\2\2\2\3=\3\2\2\2\5?\3\2\2\2\7B\3\2\2\2\tI\3\2\2\2\13R\3\2\2"+
		"\2\rk\3\2\2\2\17n\3\2\2\2\21r\3\2\2\2\23t\3\2\2\2\25v\3\2\2\2\27x\3\2"+
		"\2\2\31z\3\2\2\2\33\u0082\3\2\2\2\35\u0085\3\2\2\2\37\u008b\3\2\2\2!\u0094"+
		"\3\2\2\2#\u0098\3\2\2\2%\u009d\3\2\2\2\'\u00aa\3\2\2\2)\u00b7\3\2\2\2"+
		"+\u00bf\3\2\2\2-\u00c7\3\2\2\2/\u00ce\3\2\2\2\61\u00d6\3\2\2\2\63\u00de"+
		"\3\2\2\2\65\u00e7\3\2\2\2\67\u00ef\3\2\2\29\u00f9\3\2\2\2;\u0106\3\2\2"+
		"\2=>\t\2\2\2>\4\3\2\2\2?@\t\3\2\2@\6\3\2\2\2AC\5\3\2\2BA\3\2\2\2BC\3\2"+
		"\2\2CE\3\2\2\2DF\t\4\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\b\3"+
		"\2\2\2IK\7$\2\2JL\n\5\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3"+
		"\2\2\2OP\7$\2\2P\n\3\2\2\2QS\t\4\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3"+
		"\2\2\2UV\3\2\2\2VX\7\60\2\2WY\t\4\2\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z["+
		"\3\2\2\2[\f\3\2\2\2\\]\7x\2\2]^\7g\2\2^_\7t\2\2_`\7f\2\2`a\7c\2\2ab\7"+
		"f\2\2bc\7g\2\2cd\7k\2\2de\7t\2\2el\7q\2\2fg\7h\2\2gh\7c\2\2hi\7n\2\2i"+
		"j\7u\2\2jl\7q\2\2k\\\3\2\2\2kf\3\2\2\2l\16\3\2\2\2mo\t\6\2\2nm\3\2\2\2"+
		"op\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\20\3\2\2\2rs\7}\2\2s\22\3\2\2\2tu\7\177"+
		"\2\2u\24\3\2\2\2vw\7*\2\2w\26\3\2\2\2xy\7+\2\2y\30\3\2\2\2z{\7\"\2\2{"+
		"|\7k\2\2|}\7i\2\2}~\7w\2\2~\177\7c\2\2\177\u0080\7n\2\2\u0080\u0081\7"+
		"\"\2\2\u0081\32\3\2\2\2\u0082\u0083\7u\2\2\u0083\u0084\7g\2\2\u0084\34"+
		"\3\2\2\2\u0085\u0086\7u\2\2\u0086\u0087\7g\2\2\u0087\u0088\7p\2\2\u0088"+
		"\u0089\7c\2\2\u0089\u008a\7q\2\2\u008a\36\3\2\2\2\u008b\u008c\7g\2\2\u008c"+
		"\u008d\7p\2\2\u008d\u008e\7s\2\2\u008e\u008f\7w\2\2\u008f\u0090\7c\2\2"+
		"\u0090\u0091\7p\2\2\u0091\u0092\7v\2\2\u0092\u0093\7q\2\2\u0093 \3\2\2"+
		"\2\u0094\u0095\7\"\2\2\u0095\u0096\7g\2\2\u0096\u0097\7\"\2\2\u0097\""+
		"\3\2\2\2\u0098\u0099\7\"\2\2\u0099\u009a\7q\2\2\u009a\u009b\7w\2\2\u009b"+
		"\u009c\7\"\2\2\u009c$\3\2\2\2\u009d\u009e\7\"\2\2\u009e\u009f\7o\2\2\u009f"+
		"\u00a0\7c\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7t\2\2"+
		"\u00a3\u00a4\7K\2\2\u00a4\u00a5\7i\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7"+
		"\7c\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7\"\2\2\u00a9&\3\2\2\2\u00aa\u00ab"+
		"\7\"\2\2\u00ab\u00ac\7o\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7p\2\2\u00ae"+
		"\u00af\7q\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7K\2\2\u00b1\u00b2\7i\2\2"+
		"\u00b2\u00b3\7w\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6"+
		"\7\"\2\2\u00b6(\3\2\2\2\u00b7\u00b8\7\"\2\2\u00b8\u00b9\7o\2\2\u00b9\u00ba"+
		"\7c\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7t\2\2\u00bd"+
		"\u00be\7\"\2\2\u00be*\3\2\2\2\u00bf\u00c0\7\"\2\2\u00c0\u00c1\7o\2\2\u00c1"+
		"\u00c2\7g\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7t\2\2"+
		"\u00c5\u00c6\7\"\2\2\u00c6,\3\2\2\2\u00c7\u00c8\7\"\2\2\u00c8\u00c9\7"+
		"o\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd"+
		"\7\"\2\2\u00cd.\3\2\2\2\u00ce\u00cf\7\"\2\2\u00cf\u00d0\7o\2\2\u00d0\u00d1"+
		"\7g\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7u\2\2\u00d4"+
		"\u00d5\7\"\2\2\u00d5\60\3\2\2\2\u00d6\u00d7\7\"\2\2\u00d7\u00d8\7x\2\2"+
		"\u00d8\u00d9\7g\2\2\u00d9\u00da\7|\2\2\u00da\u00db\7g\2\2\u00db\u00dc"+
		"\7u\2\2\u00dc\u00dd\7\"\2\2\u00dd\62\3\2\2\2\u00de\u00df\7\"\2\2\u00df"+
		"\u00e0\7f\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7x\2\2\u00e2\u00e3\7k\2\2"+
		"\u00e3\u00e4\7f\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7\"\2\2\u00e6\64\3"+
		"\2\2\2\u00e7\u00e8\7\"\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7g\2\2\u00ea"+
		"\u00eb\7u\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7\"\2"+
		"\2\u00ee\66\3\2\2\2\u00ef\u00f0\7\"\2\2\u00f0\u00f1\7o\2\2\u00f1\u00f2"+
		"\7c\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7O\2\2\u00f5"+
		"\u00f6\7c\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7u\2\2\u00f88\3\2\2\2\u00f9"+
		"\u00fa\7\"\2\2\u00fa\u00fb\7o\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7p\2"+
		"\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100\7O\2\2\u0100\u0101"+
		"\7g\2\2\u0101\u0102\7p\2\2\u0102\u0103\7q\2\2\u0103\u0104\7u\2\2\u0104"+
		":\3\2\2\2\u0105\u0107\t\7\2\2\u0106\u0105\3\2\2\2\u0107\u0108\3\2\2\2"+
		"\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b"+
		"\b\36\2\2\u010b<\3\2\2\2\13\2BGMTZkp\u0108\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}