class Lexer(input: String) {
    private val tokens = mutableListOf<String>()
    private val patterns = mapOf(
        "OPEN_TAG" to Regex("<Disum\\.No\\.Zam>"),
        "USE" to Regex("use\\s+[a-zA-Z]+\\(\\)")
    )

    init {
        tokenize(input)
    }

    private fun tokenize(input: String) {
        patterns.forEach { (name, regex) ->
            regex.findAll(input).forEach { match ->
                tokens.add(name)
            }
        }
    }

    fun getTokens() = tokens
}
