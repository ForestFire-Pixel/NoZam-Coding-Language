class NoZamCompiler:
    @staticmethod
    def compile(code):
        # Check if code starts with the required tag
        if not code.startswith("<Disum.No.Zam>"):
            raise ValueError("NoZam code must start with <Disum.No.Zam>")
        
        # Replace custom NoZam functions with Python equivalents
        compiled_code = code.replace("use AlertBetter()", "AlertBetter.show_alert('Hello from NoZam!')")
        # Add more translations for each library or function
        
        return compiled_code
      
