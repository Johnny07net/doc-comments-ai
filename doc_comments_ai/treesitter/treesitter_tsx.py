from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter import Treesitter
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry

import tree_sitter

class TreesitterTSX(Treesitter):
    def __init__(self):
        super().__init__(
            Language.TSX, "function_declaration", "identifier", "comment"
        )
        
    def _query_all_methods(
        self,
        node: tree_sitter.Node,
    ):
        methods = []
        if node.type in {self.method_declaration_identifier,"jsx_element"}:
            doc_comment_node = None
            if (
                node.prev_named_sibling
                and node.prev_named_sibling.type == self.doc_comment_identifier
            ):
                doc_comment_node = node.prev_named_sibling.text.decode()
            methods.append({"method": node, "doc_comment": doc_comment_node})
        else:
            for child in node.children:
                methods.extend(self._query_all_methods(child))
        return methods

    def _query_method_name(self, node: tree_sitter.Node):
        if node.type in {self.method_declaration_identifier,"jsx_element"}:
            for child in node.children:
                if child.type == self.method_name_identifier:
                    return child.text.decode()
        return None

# Register the TreesitterJava class in the registry
TreesitterRegistry.register_treesitter(Language.TSX, TreesitterTSX)
