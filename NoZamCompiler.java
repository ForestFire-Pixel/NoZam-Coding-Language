public class NoZamCompiler {
    public String compileToJavaScript(String noZamCode) {
        // Convert NoZam syntax to JavaScript equivalent
        return noZamCode.replace("use AlertBetter()", "alert('Better Alert!');");
    }
}
