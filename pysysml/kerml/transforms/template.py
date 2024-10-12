from lark import Transformer, v_args, Tree


class KerMLTransTemplate(Transformer):
    @v_args(tree=True)
    def explicit_identification_with_short(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def explicit_identification_plain(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_recursive_membership_import(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def recursive_membership_import(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_recursive_namespace_import(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def recursive_namespace_import(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def abstract_type_prefix(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_abstract_type_prefix(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def all_classifier_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_all_classifier_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_declaration_idx(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_declaration_spc(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_declaration_coj(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def fv_bind(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def fv_initial(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def fv_default_bind(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def fv_default_initial(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def start(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def identification(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def relationship_body(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def dependency(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def dependency_annotation_list(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def dependency_list(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def comment(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def comment_prefix(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def comment_about_list(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def documentation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def locale(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def textual_representation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def textual_representation_rep(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def root_namespace(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def namespace(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def namespace_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def namespace_body(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def member_prefix(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def visibility_indicator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_feature_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def namespace_feature_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def alias_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def qualified_name(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def import_statement(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def import_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def filter_package_list(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def specialization_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def conjugation_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def disjoining_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def unioning_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def intersecting_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def differencing_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_body(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def specialization(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def conjugation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def disjoining(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_feature_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_feature_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def classifier(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def superclassing_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def subclassification(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_prefix(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_direction(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_relationship_type(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def chaining_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def inverting_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_featuring_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_specialization_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def typings(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def typed_by(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def subsettings(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def subsets(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def references(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def redefinitions(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def redefines(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_typing(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def subsetting(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def redefinition(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_chain(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_inverting(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_featuring(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def data_type(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def class_statement(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def structure(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def association(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def association_structure(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def connector(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def binary_connector_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def nary_connector_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def connector_end(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def binding_connector(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def binding_connector_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def succession(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def succession_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def behavior(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def step(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_body(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_body_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def return_feature_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def result_expression_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def predicate(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def boolean_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def invariant(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def conditional_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def conditional_binary_operator_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def conditional_binary_operator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def binary_operator_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def binary_operator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def unary_operator_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def unary_operator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def classification_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def classification_test_operator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def cast_operator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metaclassification_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def meta_classification_test_operator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def meta_cast_operator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def extent_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def bracket_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def index_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def sequence_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def sequence_expression_list(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def sequence_operator_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_chain_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def collect_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def select_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_operation_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def null_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_access_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def invocation_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def argument_list(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def positional_argument_list(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def named_argument_list(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def named_argument(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def body_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def expression_body(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def literal_boolean(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def literal_string(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def literal_integer(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def literal_real(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def literal_infinity(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def interaction(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_flow(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def succession_item_flow(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_flow_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_feature(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_feature_specialization_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_flow_end(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity_subset(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity_range(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity_bounds(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metaclass(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def prefix_metadata_annotation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def prefix_metadata_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_feature(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_feature_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_body(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_body_feature(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def package(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def library_package(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def package_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def package_body(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def element_filter_member(self, tree: Tree):
        return tree

