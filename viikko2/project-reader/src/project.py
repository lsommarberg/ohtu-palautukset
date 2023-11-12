class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        if dependencies:
            return "\n".join(["- " + dependency for dependency in dependencies])
        else:
            return "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\nAuthors: \n{self._stringify_dependencies(self.authors)}"
            f"\nDependencies: \n{self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: \n{self._stringify_dependencies(self.dev_dependencies)}"
        )
