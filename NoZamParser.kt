class Parser(private val tokens: List<String>) {
    fun parse() {
        if (tokens.first() != "OPEN_TAG") {
            throw IllegalArgumentException("Code must start with <Disum.No.Zam>")
        }
        // Additional parsing rules for functions, keywords, etc.
    }
}
