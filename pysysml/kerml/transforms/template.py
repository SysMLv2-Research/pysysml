from lark import Transformer, v_args, Tree


class KerMLTransTemplate(Transformer):
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
    def relationship_owned_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_related_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def dependency(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def annotation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_annotation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def annotating_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def comment(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def documentation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def textual_representation(self, tree: Tree):
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
    def namespace_body_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def member_prefix(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def visibility_indicator(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def namespace_member(self, tree: Tree):
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
    def membership_import(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def namespace_import(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def filter_package(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def filter_package_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def member_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_feature_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_prefix(self, tree: Tree):
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
    def type_relationship_part(self, tree: Tree):
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
    def type_body_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def specialization(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_specialization(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def specific_type(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def general_type(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def conjugation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_conjugation(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def disjoining(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_disjoining(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def unioning(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def intersecting(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def differencing(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_member(self, tree: Tree):
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
    def classifier_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def superclassing_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def subclassification(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_subclassification(self, tree: Tree):
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
    def feature_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_identification(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_relationship_part(self, tree: Tree):
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
    def feature_specialization(self, tree: Tree):
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
    def owned_feature_typing(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def subsetting(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_subsetting(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_reference_subsetting(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def redefinition(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_redefinition(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_feature_chain(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_chain(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_feature_chaining(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_inverting(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_feature_inverting(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_featuring(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_type_featuring(self, tree: Tree):
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
    def connector_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def binary_connector_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def nary_connector_declaration(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def connector_end_member(self, tree: Tree):
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
    def owned_expression_reference_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_expression_reference(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_expression_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_expression(self, tree: Tree):
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
    def argument_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def argument(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def argument_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def argument_expression_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def argument_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def argument_expression_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_argument_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_argument(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_reference(self, tree: Tree):
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
    def type_reference_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_result_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def type_reference(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def reference_typing(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def primary_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def primary_argument_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def primary_argument(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def primary_argument_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_feature_chain_primary_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_feature_chain_primary_argument_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_feature_chain_primary_argument(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def non_feature_chain_primary_argument_member(self, tree: Tree):
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
    def sequence_expression_list_member(self, tree: Tree):
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
    def body_argument_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def body_argument(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def body_argument_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_reference_argument_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_reference_argument(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_reference_argument_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_reference_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_reference_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def function_reference(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_chain_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_feature_chain_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def base_expression(self, tree: Tree):
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
    def named_argument_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def named_argument(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def parameter_redefinition(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def body_expression(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def body_expression_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def expression_body(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def literal_expression(self, tree: Tree):
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
    def item_feature_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_feature(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_feature_specialization_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_flow_end_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_flow_end(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_flow_feature_member(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_flow_feature(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def item_flow_redefinition(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def value_part(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def feature_value(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity_subset(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity_range(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_multiplicity(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def owned_multiplicity_range(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity_bounds(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def multiplicity_expression_member(self, tree: Tree):
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
    def prefix_metadata_feature(self, tree: Tree):
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
    def metadata_body_element(self, tree: Tree):
        return tree

    @v_args(tree=True)
    def metadata_body_feature_member(self, tree: Tree):
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

