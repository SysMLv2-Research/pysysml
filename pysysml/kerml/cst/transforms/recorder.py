from lark import v_args, Tree

from .template import KerMLTransTemplate


class KerMLTransRecorder(KerMLTransTemplate):
    def __init__(self, visit_tokens: bool = True):
        KerMLTransTemplate.__init__(self, visit_tokens=visit_tokens)
        self._rules_set = set()
        self.rules = []

    @v_args(tree=True)
    def explicit_identification_with_short(self, tree: Tree):
        if 'explicit_identification_with_short' not in self._rules_set:
            self._rules_set.add('explicit_identification_with_short')
            self.rules.append('explicit_identification_with_short')
        return KerMLTransTemplate.explicit_identification_with_short(self, tree)

    @v_args(tree=True)
    def explicit_identification_plain(self, tree: Tree):
        if 'explicit_identification_plain' not in self._rules_set:
            self._rules_set.add('explicit_identification_plain')
            self.rules.append('explicit_identification_plain')
        return KerMLTransTemplate.explicit_identification_plain(self, tree)

    @v_args(tree=True)
    def non_recursive_membership_import(self, tree: Tree):
        if 'non_recursive_membership_import' not in self._rules_set:
            self._rules_set.add('non_recursive_membership_import')
            self.rules.append('non_recursive_membership_import')
        return KerMLTransTemplate.non_recursive_membership_import(self, tree)

    @v_args(tree=True)
    def recursive_membership_import(self, tree: Tree):
        if 'recursive_membership_import' not in self._rules_set:
            self._rules_set.add('recursive_membership_import')
            self.rules.append('recursive_membership_import')
        return KerMLTransTemplate.recursive_membership_import(self, tree)

    @v_args(tree=True)
    def non_recursive_namespace_import(self, tree: Tree):
        if 'non_recursive_namespace_import' not in self._rules_set:
            self._rules_set.add('non_recursive_namespace_import')
            self.rules.append('non_recursive_namespace_import')
        return KerMLTransTemplate.non_recursive_namespace_import(self, tree)

    @v_args(tree=True)
    def recursive_namespace_import(self, tree: Tree):
        if 'recursive_namespace_import' not in self._rules_set:
            self._rules_set.add('recursive_namespace_import')
            self.rules.append('recursive_namespace_import')
        return KerMLTransTemplate.recursive_namespace_import(self, tree)

    @v_args(tree=True)
    def abstract_type_prefix(self, tree: Tree):
        if 'abstract_type_prefix' not in self._rules_set:
            self._rules_set.add('abstract_type_prefix')
            self.rules.append('abstract_type_prefix')
        return KerMLTransTemplate.abstract_type_prefix(self, tree)

    @v_args(tree=True)
    def non_abstract_type_prefix(self, tree: Tree):
        if 'non_abstract_type_prefix' not in self._rules_set:
            self._rules_set.add('non_abstract_type_prefix')
            self.rules.append('non_abstract_type_prefix')
        return KerMLTransTemplate.non_abstract_type_prefix(self, tree)

    @v_args(tree=True)
    def all_classifier_declaration(self, tree: Tree):
        if 'all_classifier_declaration' not in self._rules_set:
            self._rules_set.add('all_classifier_declaration')
            self.rules.append('all_classifier_declaration')
        return KerMLTransTemplate.all_classifier_declaration(self, tree)

    @v_args(tree=True)
    def non_all_classifier_declaration(self, tree: Tree):
        if 'non_all_classifier_declaration' not in self._rules_set:
            self._rules_set.add('non_all_classifier_declaration')
            self.rules.append('non_all_classifier_declaration')
        return KerMLTransTemplate.non_all_classifier_declaration(self, tree)

    @v_args(tree=True)
    def feature_declaration_idx(self, tree: Tree):
        if 'feature_declaration_idx' not in self._rules_set:
            self._rules_set.add('feature_declaration_idx')
            self.rules.append('feature_declaration_idx')
        return KerMLTransTemplate.feature_declaration_idx(self, tree)

    @v_args(tree=True)
    def feature_declaration_spc(self, tree: Tree):
        if 'feature_declaration_spc' not in self._rules_set:
            self._rules_set.add('feature_declaration_spc')
            self.rules.append('feature_declaration_spc')
        return KerMLTransTemplate.feature_declaration_spc(self, tree)

    @v_args(tree=True)
    def feature_declaration_coj(self, tree: Tree):
        if 'feature_declaration_coj' not in self._rules_set:
            self._rules_set.add('feature_declaration_coj')
            self.rules.append('feature_declaration_coj')
        return KerMLTransTemplate.feature_declaration_coj(self, tree)

    @v_args(tree=True)
    def all_binary_connector_declaration(self, tree: Tree):
        if 'all_binary_connector_declaration' not in self._rules_set:
            self._rules_set.add('all_binary_connector_declaration')
            self.rules.append('all_binary_connector_declaration')
        return KerMLTransTemplate.all_binary_connector_declaration(self, tree)

    @v_args(tree=True)
    def non_all_binary_connector_declaration(self, tree: Tree):
        if 'non_all_binary_connector_declaration' not in self._rules_set:
            self._rules_set.add('non_all_binary_connector_declaration')
            self.rules.append('non_all_binary_connector_declaration')
        return KerMLTransTemplate.non_all_binary_connector_declaration(self, tree)

    @v_args(tree=True)
    def sequence_expression_list_standalone(self, tree: Tree):
        if 'sequence_expression_list_standalone' not in self._rules_set:
            self._rules_set.add('sequence_expression_list_standalone')
            self.rules.append('sequence_expression_list_standalone')
        return KerMLTransTemplate.sequence_expression_list_standalone(self, tree)

    @v_args(tree=True)
    def function_operation_expression_standalone(self, tree: Tree):
        if 'function_operation_expression_standalone' not in self._rules_set:
            self._rules_set.add('function_operation_expression_standalone')
            self.rules.append('function_operation_expression_standalone')
        return KerMLTransTemplate.function_operation_expression_standalone(self, tree)

    @v_args(tree=True)
    def function_operation_expression_arglist(self, tree: Tree):
        if 'function_operation_expression_arglist' not in self._rules_set:
            self._rules_set.add('function_operation_expression_arglist')
            self.rules.append('function_operation_expression_arglist')
        return KerMLTransTemplate.function_operation_expression_arglist(self, tree)

    @v_args(tree=True)
    def item_flow_declaration_dec(self, tree: Tree):
        if 'item_flow_declaration_dec' not in self._rules_set:
            self._rules_set.add('item_flow_declaration_dec')
            self.rules.append('item_flow_declaration_dec')
        return KerMLTransTemplate.item_flow_declaration_dec(self, tree)

    @v_args(tree=True)
    def item_flow_declaration_simple(self, tree: Tree):
        if 'item_flow_declaration_simple' not in self._rules_set:
            self._rules_set.add('item_flow_declaration_simple')
            self.rules.append('item_flow_declaration_simple')
        return KerMLTransTemplate.item_flow_declaration_simple(self, tree)

    @v_args(tree=True)
    def item_feature_idx(self, tree: Tree):
        if 'item_feature_idx' not in self._rules_set:
            self._rules_set.add('item_feature_idx')
            self.rules.append('item_feature_idx')
        return KerMLTransTemplate.item_feature_idx(self, tree)

    @v_args(tree=True)
    def item_feature_ft(self, tree: Tree):
        if 'item_feature_ft' not in self._rules_set:
            self._rules_set.add('item_feature_ft')
            self.rules.append('item_feature_ft')
        return KerMLTransTemplate.item_feature_ft(self, tree)

    @v_args(tree=True)
    def item_feature_m(self, tree: Tree):
        if 'item_feature_m' not in self._rules_set:
            self._rules_set.add('item_feature_m')
            self.rules.append('item_feature_m')
        return KerMLTransTemplate.item_feature_m(self, tree)

    @v_args(tree=True)
    def fv_bind(self, tree: Tree):
        if 'fv_bind' not in self._rules_set:
            self._rules_set.add('fv_bind')
            self.rules.append('fv_bind')
        return KerMLTransTemplate.fv_bind(self, tree)

    @v_args(tree=True)
    def fv_initial(self, tree: Tree):
        if 'fv_initial' not in self._rules_set:
            self._rules_set.add('fv_initial')
            self.rules.append('fv_initial')
        return KerMLTransTemplate.fv_initial(self, tree)

    @v_args(tree=True)
    def fv_default_bind(self, tree: Tree):
        if 'fv_default_bind' not in self._rules_set:
            self._rules_set.add('fv_default_bind')
            self.rules.append('fv_default_bind')
        return KerMLTransTemplate.fv_default_bind(self, tree)

    @v_args(tree=True)
    def fv_default_initial(self, tree: Tree):
        if 'fv_default_initial' not in self._rules_set:
            self._rules_set.add('fv_default_initial')
            self.rules.append('fv_default_initial')
        return KerMLTransTemplate.fv_default_initial(self, tree)

    @v_args(tree=True)
    def start(self, tree: Tree):
        if 'start' not in self._rules_set:
            self._rules_set.add('start')
            self.rules.append('start')
        return KerMLTransTemplate.start(self, tree)

    @v_args(tree=True)
    def identification(self, tree: Tree):
        if 'identification' not in self._rules_set:
            self._rules_set.add('identification')
            self.rules.append('identification')
        return KerMLTransTemplate.identification(self, tree)

    @v_args(tree=True)
    def relationship_body(self, tree: Tree):
        if 'relationship_body' not in self._rules_set:
            self._rules_set.add('relationship_body')
            self.rules.append('relationship_body')
        return KerMLTransTemplate.relationship_body(self, tree)

    @v_args(tree=True)
    def dependency(self, tree: Tree):
        if 'dependency' not in self._rules_set:
            self._rules_set.add('dependency')
            self.rules.append('dependency')
        return KerMLTransTemplate.dependency(self, tree)

    @v_args(tree=True)
    def dependency_annotation_list(self, tree: Tree):
        if 'dependency_annotation_list' not in self._rules_set:
            self._rules_set.add('dependency_annotation_list')
            self.rules.append('dependency_annotation_list')
        return KerMLTransTemplate.dependency_annotation_list(self, tree)

    @v_args(tree=True)
    def dependency_list(self, tree: Tree):
        if 'dependency_list' not in self._rules_set:
            self._rules_set.add('dependency_list')
            self.rules.append('dependency_list')
        return KerMLTransTemplate.dependency_list(self, tree)

    @v_args(tree=True)
    def comment(self, tree: Tree):
        if 'comment' not in self._rules_set:
            self._rules_set.add('comment')
            self.rules.append('comment')
        return KerMLTransTemplate.comment(self, tree)

    @v_args(tree=True)
    def comment_prefix(self, tree: Tree):
        if 'comment_prefix' not in self._rules_set:
            self._rules_set.add('comment_prefix')
            self.rules.append('comment_prefix')
        return KerMLTransTemplate.comment_prefix(self, tree)

    @v_args(tree=True)
    def comment_about_list(self, tree: Tree):
        if 'comment_about_list' not in self._rules_set:
            self._rules_set.add('comment_about_list')
            self.rules.append('comment_about_list')
        return KerMLTransTemplate.comment_about_list(self, tree)

    @v_args(tree=True)
    def documentation(self, tree: Tree):
        if 'documentation' not in self._rules_set:
            self._rules_set.add('documentation')
            self.rules.append('documentation')
        return KerMLTransTemplate.documentation(self, tree)

    @v_args(tree=True)
    def locale(self, tree: Tree):
        if 'locale' not in self._rules_set:
            self._rules_set.add('locale')
            self.rules.append('locale')
        return KerMLTransTemplate.locale(self, tree)

    @v_args(tree=True)
    def textual_representation(self, tree: Tree):
        if 'textual_representation' not in self._rules_set:
            self._rules_set.add('textual_representation')
            self.rules.append('textual_representation')
        return KerMLTransTemplate.textual_representation(self, tree)

    @v_args(tree=True)
    def textual_representation_rep(self, tree: Tree):
        if 'textual_representation_rep' not in self._rules_set:
            self._rules_set.add('textual_representation_rep')
            self.rules.append('textual_representation_rep')
        return KerMLTransTemplate.textual_representation_rep(self, tree)

    @v_args(tree=True)
    def root_namespace(self, tree: Tree):
        if 'root_namespace' not in self._rules_set:
            self._rules_set.add('root_namespace')
            self.rules.append('root_namespace')
        return KerMLTransTemplate.root_namespace(self, tree)

    @v_args(tree=True)
    def namespace(self, tree: Tree):
        if 'namespace' not in self._rules_set:
            self._rules_set.add('namespace')
            self.rules.append('namespace')
        return KerMLTransTemplate.namespace(self, tree)

    @v_args(tree=True)
    def namespace_declaration(self, tree: Tree):
        if 'namespace_declaration' not in self._rules_set:
            self._rules_set.add('namespace_declaration')
            self.rules.append('namespace_declaration')
        return KerMLTransTemplate.namespace_declaration(self, tree)

    @v_args(tree=True)
    def namespace_body(self, tree: Tree):
        if 'namespace_body' not in self._rules_set:
            self._rules_set.add('namespace_body')
            self.rules.append('namespace_body')
        return KerMLTransTemplate.namespace_body(self, tree)

    @v_args(tree=True)
    def member_prefix(self, tree: Tree):
        if 'member_prefix' not in self._rules_set:
            self._rules_set.add('member_prefix')
            self.rules.append('member_prefix')
        return KerMLTransTemplate.member_prefix(self, tree)

    @v_args(tree=True)
    def visibility_indicator(self, tree: Tree):
        if 'visibility_indicator' not in self._rules_set:
            self._rules_set.add('visibility_indicator')
            self.rules.append('visibility_indicator')
        return KerMLTransTemplate.visibility_indicator(self, tree)

    @v_args(tree=True)
    def non_feature_member(self, tree: Tree):
        if 'non_feature_member' not in self._rules_set:
            self._rules_set.add('non_feature_member')
            self.rules.append('non_feature_member')
        return KerMLTransTemplate.non_feature_member(self, tree)

    @v_args(tree=True)
    def namespace_feature_member(self, tree: Tree):
        if 'namespace_feature_member' not in self._rules_set:
            self._rules_set.add('namespace_feature_member')
            self.rules.append('namespace_feature_member')
        return KerMLTransTemplate.namespace_feature_member(self, tree)

    @v_args(tree=True)
    def alias_member(self, tree: Tree):
        if 'alias_member' not in self._rules_set:
            self._rules_set.add('alias_member')
            self.rules.append('alias_member')
        return KerMLTransTemplate.alias_member(self, tree)

    @v_args(tree=True)
    def qualified_name(self, tree: Tree):
        if 'qualified_name' not in self._rules_set:
            self._rules_set.add('qualified_name')
            self.rules.append('qualified_name')
        return KerMLTransTemplate.qualified_name(self, tree)

    @v_args(tree=True)
    def import_statement(self, tree: Tree):
        if 'import_statement' not in self._rules_set:
            self._rules_set.add('import_statement')
            self.rules.append('import_statement')
        return KerMLTransTemplate.import_statement(self, tree)

    @v_args(tree=True)
    def import_declaration(self, tree: Tree):
        if 'import_declaration' not in self._rules_set:
            self._rules_set.add('import_declaration')
            self.rules.append('import_declaration')
        return KerMLTransTemplate.import_declaration(self, tree)

    @v_args(tree=True)
    def filter_package_list(self, tree: Tree):
        if 'filter_package_list' not in self._rules_set:
            self._rules_set.add('filter_package_list')
            self.rules.append('filter_package_list')
        return KerMLTransTemplate.filter_package_list(self, tree)

    @v_args(tree=True)
    def type(self, tree: Tree):
        if 'type' not in self._rules_set:
            self._rules_set.add('type')
            self.rules.append('type')
        return KerMLTransTemplate.type(self, tree)

    @v_args(tree=True)
    def type_declaration(self, tree: Tree):
        if 'type_declaration' not in self._rules_set:
            self._rules_set.add('type_declaration')
            self.rules.append('type_declaration')
        return KerMLTransTemplate.type_declaration(self, tree)

    @v_args(tree=True)
    def specialization_part(self, tree: Tree):
        if 'specialization_part' not in self._rules_set:
            self._rules_set.add('specialization_part')
            self.rules.append('specialization_part')
        return KerMLTransTemplate.specialization_part(self, tree)

    @v_args(tree=True)
    def conjugation_part(self, tree: Tree):
        if 'conjugation_part' not in self._rules_set:
            self._rules_set.add('conjugation_part')
            self.rules.append('conjugation_part')
        return KerMLTransTemplate.conjugation_part(self, tree)

    @v_args(tree=True)
    def disjoining_part(self, tree: Tree):
        if 'disjoining_part' not in self._rules_set:
            self._rules_set.add('disjoining_part')
            self.rules.append('disjoining_part')
        return KerMLTransTemplate.disjoining_part(self, tree)

    @v_args(tree=True)
    def unioning_part(self, tree: Tree):
        if 'unioning_part' not in self._rules_set:
            self._rules_set.add('unioning_part')
            self.rules.append('unioning_part')
        return KerMLTransTemplate.unioning_part(self, tree)

    @v_args(tree=True)
    def intersecting_part(self, tree: Tree):
        if 'intersecting_part' not in self._rules_set:
            self._rules_set.add('intersecting_part')
            self.rules.append('intersecting_part')
        return KerMLTransTemplate.intersecting_part(self, tree)

    @v_args(tree=True)
    def differencing_part(self, tree: Tree):
        if 'differencing_part' not in self._rules_set:
            self._rules_set.add('differencing_part')
            self.rules.append('differencing_part')
        return KerMLTransTemplate.differencing_part(self, tree)

    @v_args(tree=True)
    def type_body(self, tree: Tree):
        if 'type_body' not in self._rules_set:
            self._rules_set.add('type_body')
            self.rules.append('type_body')
        return KerMLTransTemplate.type_body(self, tree)

    @v_args(tree=True)
    def specialization(self, tree: Tree):
        if 'specialization' not in self._rules_set:
            self._rules_set.add('specialization')
            self.rules.append('specialization')
        return KerMLTransTemplate.specialization(self, tree)

    @v_args(tree=True)
    def conjugation(self, tree: Tree):
        if 'conjugation' not in self._rules_set:
            self._rules_set.add('conjugation')
            self.rules.append('conjugation')
        return KerMLTransTemplate.conjugation(self, tree)

    @v_args(tree=True)
    def disjoining(self, tree: Tree):
        if 'disjoining' not in self._rules_set:
            self._rules_set.add('disjoining')
            self.rules.append('disjoining')
        return KerMLTransTemplate.disjoining(self, tree)

    @v_args(tree=True)
    def type_feature_member(self, tree: Tree):
        if 'type_feature_member' not in self._rules_set:
            self._rules_set.add('type_feature_member')
            self.rules.append('type_feature_member')
        return KerMLTransTemplate.type_feature_member(self, tree)

    @v_args(tree=True)
    def owned_feature_member(self, tree: Tree):
        if 'owned_feature_member' not in self._rules_set:
            self._rules_set.add('owned_feature_member')
            self.rules.append('owned_feature_member')
        return KerMLTransTemplate.owned_feature_member(self, tree)

    @v_args(tree=True)
    def classifier(self, tree: Tree):
        if 'classifier' not in self._rules_set:
            self._rules_set.add('classifier')
            self.rules.append('classifier')
        return KerMLTransTemplate.classifier(self, tree)

    @v_args(tree=True)
    def superclassing_part(self, tree: Tree):
        if 'superclassing_part' not in self._rules_set:
            self._rules_set.add('superclassing_part')
            self.rules.append('superclassing_part')
        return KerMLTransTemplate.superclassing_part(self, tree)

    @v_args(tree=True)
    def subclassification(self, tree: Tree):
        if 'subclassification' not in self._rules_set:
            self._rules_set.add('subclassification')
            self.rules.append('subclassification')
        return KerMLTransTemplate.subclassification(self, tree)

    @v_args(tree=True)
    def feature(self, tree: Tree):
        if 'feature' not in self._rules_set:
            self._rules_set.add('feature')
            self.rules.append('feature')
        return KerMLTransTemplate.feature(self, tree)

    @v_args(tree=True)
    def feature_prefix(self, tree: Tree):
        if 'feature_prefix' not in self._rules_set:
            self._rules_set.add('feature_prefix')
            self.rules.append('feature_prefix')
        return KerMLTransTemplate.feature_prefix(self, tree)

    @v_args(tree=True)
    def feature_direction(self, tree: Tree):
        if 'feature_direction' not in self._rules_set:
            self._rules_set.add('feature_direction')
            self.rules.append('feature_direction')
        return KerMLTransTemplate.feature_direction(self, tree)

    @v_args(tree=True)
    def feature_relationship_type(self, tree: Tree):
        if 'feature_relationship_type' not in self._rules_set:
            self._rules_set.add('feature_relationship_type')
            self.rules.append('feature_relationship_type')
        return KerMLTransTemplate.feature_relationship_type(self, tree)

    @v_args(tree=True)
    def feature_declaration(self, tree: Tree):
        if 'feature_declaration' not in self._rules_set:
            self._rules_set.add('feature_declaration')
            self.rules.append('feature_declaration')
        return KerMLTransTemplate.feature_declaration(self, tree)

    @v_args(tree=True)
    def chaining_part(self, tree: Tree):
        if 'chaining_part' not in self._rules_set:
            self._rules_set.add('chaining_part')
            self.rules.append('chaining_part')
        return KerMLTransTemplate.chaining_part(self, tree)

    @v_args(tree=True)
    def inverting_part(self, tree: Tree):
        if 'inverting_part' not in self._rules_set:
            self._rules_set.add('inverting_part')
            self.rules.append('inverting_part')
        return KerMLTransTemplate.inverting_part(self, tree)

    @v_args(tree=True)
    def type_featuring_part(self, tree: Tree):
        if 'type_featuring_part' not in self._rules_set:
            self._rules_set.add('type_featuring_part')
            self.rules.append('type_featuring_part')
        return KerMLTransTemplate.type_featuring_part(self, tree)

    @v_args(tree=True)
    def feature_specialization_part(self, tree: Tree):
        if 'feature_specialization_part' not in self._rules_set:
            self._rules_set.add('feature_specialization_part')
            self.rules.append('feature_specialization_part')
        return KerMLTransTemplate.feature_specialization_part(self, tree)

    @v_args(tree=True)
    def multiplicity_part(self, tree: Tree):
        if 'multiplicity_part' not in self._rules_set:
            self._rules_set.add('multiplicity_part')
            self.rules.append('multiplicity_part')
        return KerMLTransTemplate.multiplicity_part(self, tree)

    @v_args(tree=True)
    def typings(self, tree: Tree):
        if 'typings' not in self._rules_set:
            self._rules_set.add('typings')
            self.rules.append('typings')
        return KerMLTransTemplate.typings(self, tree)

    @v_args(tree=True)
    def typed_by(self, tree: Tree):
        if 'typed_by' not in self._rules_set:
            self._rules_set.add('typed_by')
            self.rules.append('typed_by')
        return KerMLTransTemplate.typed_by(self, tree)

    @v_args(tree=True)
    def subsettings(self, tree: Tree):
        if 'subsettings' not in self._rules_set:
            self._rules_set.add('subsettings')
            self.rules.append('subsettings')
        return KerMLTransTemplate.subsettings(self, tree)

    @v_args(tree=True)
    def subsets(self, tree: Tree):
        if 'subsets' not in self._rules_set:
            self._rules_set.add('subsets')
            self.rules.append('subsets')
        return KerMLTransTemplate.subsets(self, tree)

    @v_args(tree=True)
    def references(self, tree: Tree):
        if 'references' not in self._rules_set:
            self._rules_set.add('references')
            self.rules.append('references')
        return KerMLTransTemplate.references(self, tree)

    @v_args(tree=True)
    def redefinitions(self, tree: Tree):
        if 'redefinitions' not in self._rules_set:
            self._rules_set.add('redefinitions')
            self.rules.append('redefinitions')
        return KerMLTransTemplate.redefinitions(self, tree)

    @v_args(tree=True)
    def redefines(self, tree: Tree):
        if 'redefines' not in self._rules_set:
            self._rules_set.add('redefines')
            self.rules.append('redefines')
        return KerMLTransTemplate.redefines(self, tree)

    @v_args(tree=True)
    def feature_typing(self, tree: Tree):
        if 'feature_typing' not in self._rules_set:
            self._rules_set.add('feature_typing')
            self.rules.append('feature_typing')
        return KerMLTransTemplate.feature_typing(self, tree)

    @v_args(tree=True)
    def subsetting(self, tree: Tree):
        if 'subsetting' not in self._rules_set:
            self._rules_set.add('subsetting')
            self.rules.append('subsetting')
        return KerMLTransTemplate.subsetting(self, tree)

    @v_args(tree=True)
    def redefinition(self, tree: Tree):
        if 'redefinition' not in self._rules_set:
            self._rules_set.add('redefinition')
            self.rules.append('redefinition')
        return KerMLTransTemplate.redefinition(self, tree)

    @v_args(tree=True)
    def feature_chain(self, tree: Tree):
        if 'feature_chain' not in self._rules_set:
            self._rules_set.add('feature_chain')
            self.rules.append('feature_chain')
        return KerMLTransTemplate.feature_chain(self, tree)

    @v_args(tree=True)
    def feature_inverting(self, tree: Tree):
        if 'feature_inverting' not in self._rules_set:
            self._rules_set.add('feature_inverting')
            self.rules.append('feature_inverting')
        return KerMLTransTemplate.feature_inverting(self, tree)

    @v_args(tree=True)
    def type_featuring(self, tree: Tree):
        if 'type_featuring' not in self._rules_set:
            self._rules_set.add('type_featuring')
            self.rules.append('type_featuring')
        return KerMLTransTemplate.type_featuring(self, tree)

    @v_args(tree=True)
    def data_type(self, tree: Tree):
        if 'data_type' not in self._rules_set:
            self._rules_set.add('data_type')
            self.rules.append('data_type')
        return KerMLTransTemplate.data_type(self, tree)

    @v_args(tree=True)
    def class_statement(self, tree: Tree):
        if 'class_statement' not in self._rules_set:
            self._rules_set.add('class_statement')
            self.rules.append('class_statement')
        return KerMLTransTemplate.class_statement(self, tree)

    @v_args(tree=True)
    def structure(self, tree: Tree):
        if 'structure' not in self._rules_set:
            self._rules_set.add('structure')
            self.rules.append('structure')
        return KerMLTransTemplate.structure(self, tree)

    @v_args(tree=True)
    def association(self, tree: Tree):
        if 'association' not in self._rules_set:
            self._rules_set.add('association')
            self.rules.append('association')
        return KerMLTransTemplate.association(self, tree)

    @v_args(tree=True)
    def association_structure(self, tree: Tree):
        if 'association_structure' not in self._rules_set:
            self._rules_set.add('association_structure')
            self.rules.append('association_structure')
        return KerMLTransTemplate.association_structure(self, tree)

    @v_args(tree=True)
    def connector(self, tree: Tree):
        if 'connector' not in self._rules_set:
            self._rules_set.add('connector')
            self.rules.append('connector')
        return KerMLTransTemplate.connector(self, tree)

    @v_args(tree=True)
    def value_connector_declaration(self, tree: Tree):
        if 'value_connector_declaration' not in self._rules_set:
            self._rules_set.add('value_connector_declaration')
            self.rules.append('value_connector_declaration')
        return KerMLTransTemplate.value_connector_declaration(self, tree)

    @v_args(tree=True)
    def nary_connector_declaration(self, tree: Tree):
        if 'nary_connector_declaration' not in self._rules_set:
            self._rules_set.add('nary_connector_declaration')
            self.rules.append('nary_connector_declaration')
        return KerMLTransTemplate.nary_connector_declaration(self, tree)

    @v_args(tree=True)
    def connector_end(self, tree: Tree):
        if 'connector_end' not in self._rules_set:
            self._rules_set.add('connector_end')
            self.rules.append('connector_end')
        return KerMLTransTemplate.connector_end(self, tree)

    @v_args(tree=True)
    def connector_end_to(self, tree: Tree):
        if 'connector_end_to' not in self._rules_set:
            self._rules_set.add('connector_end_to')
            self.rules.append('connector_end_to')
        return KerMLTransTemplate.connector_end_to(self, tree)

    @v_args(tree=True)
    def connector_end_name(self, tree: Tree):
        if 'connector_end_name' not in self._rules_set:
            self._rules_set.add('connector_end_name')
            self.rules.append('connector_end_name')
        return KerMLTransTemplate.connector_end_name(self, tree)

    @v_args(tree=True)
    def binding_connector(self, tree: Tree):
        if 'binding_connector' not in self._rules_set:
            self._rules_set.add('binding_connector')
            self.rules.append('binding_connector')
        return KerMLTransTemplate.binding_connector(self, tree)

    @v_args(tree=True)
    def non_declare_binding_connector_declaration(self, tree: Tree):
        if 'non_declare_binding_connector_declaration' not in self._rules_set:
            self._rules_set.add('non_declare_binding_connector_declaration')
            self.rules.append('non_declare_binding_connector_declaration')
        return KerMLTransTemplate.non_declare_binding_connector_declaration(self, tree)

    @v_args(tree=True)
    def declare_binding_connector_declaration(self, tree: Tree):
        if 'declare_binding_connector_declaration' not in self._rules_set:
            self._rules_set.add('declare_binding_connector_declaration')
            self.rules.append('declare_binding_connector_declaration')
        return KerMLTransTemplate.declare_binding_connector_declaration(self, tree)

    @v_args(tree=True)
    def succession(self, tree: Tree):
        if 'succession' not in self._rules_set:
            self._rules_set.add('succession')
            self.rules.append('succession')
        return KerMLTransTemplate.succession(self, tree)

    @v_args(tree=True)
    def non_declare_succession_declaration(self, tree: Tree):
        if 'non_declare_succession_declaration' not in self._rules_set:
            self._rules_set.add('non_declare_succession_declaration')
            self.rules.append('non_declare_succession_declaration')
        return KerMLTransTemplate.non_declare_succession_declaration(self, tree)

    @v_args(tree=True)
    def declare_succession_declaration(self, tree: Tree):
        if 'declare_succession_declaration' not in self._rules_set:
            self._rules_set.add('declare_succession_declaration')
            self.rules.append('declare_succession_declaration')
        return KerMLTransTemplate.declare_succession_declaration(self, tree)

    @v_args(tree=True)
    def behavior(self, tree: Tree):
        if 'behavior' not in self._rules_set:
            self._rules_set.add('behavior')
            self.rules.append('behavior')
        return KerMLTransTemplate.behavior(self, tree)

    @v_args(tree=True)
    def step(self, tree: Tree):
        if 'step' not in self._rules_set:
            self._rules_set.add('step')
            self.rules.append('step')
        return KerMLTransTemplate.step(self, tree)

    @v_args(tree=True)
    def function(self, tree: Tree):
        if 'function' not in self._rules_set:
            self._rules_set.add('function')
            self.rules.append('function')
        return KerMLTransTemplate.function(self, tree)

    @v_args(tree=True)
    def function_body(self, tree: Tree):
        if 'function_body' not in self._rules_set:
            self._rules_set.add('function_body')
            self.rules.append('function_body')
        return KerMLTransTemplate.function_body(self, tree)

    @v_args(tree=True)
    def function_body_part(self, tree: Tree):
        if 'function_body_part' not in self._rules_set:
            self._rules_set.add('function_body_part')
            self.rules.append('function_body_part')
        return KerMLTransTemplate.function_body_part(self, tree)

    @v_args(tree=True)
    def return_feature_member(self, tree: Tree):
        if 'return_feature_member' not in self._rules_set:
            self._rules_set.add('return_feature_member')
            self.rules.append('return_feature_member')
        return KerMLTransTemplate.return_feature_member(self, tree)

    @v_args(tree=True)
    def result_expression_member(self, tree: Tree):
        if 'result_expression_member' not in self._rules_set:
            self._rules_set.add('result_expression_member')
            self.rules.append('result_expression_member')
        return KerMLTransTemplate.result_expression_member(self, tree)

    @v_args(tree=True)
    def expression(self, tree: Tree):
        if 'expression' not in self._rules_set:
            self._rules_set.add('expression')
            self.rules.append('expression')
        return KerMLTransTemplate.expression(self, tree)

    @v_args(tree=True)
    def predicate(self, tree: Tree):
        if 'predicate' not in self._rules_set:
            self._rules_set.add('predicate')
            self.rules.append('predicate')
        return KerMLTransTemplate.predicate(self, tree)

    @v_args(tree=True)
    def boolean_expression(self, tree: Tree):
        if 'boolean_expression' not in self._rules_set:
            self._rules_set.add('boolean_expression')
            self.rules.append('boolean_expression')
        return KerMLTransTemplate.boolean_expression(self, tree)

    @v_args(tree=True)
    def invariant(self, tree: Tree):
        if 'invariant' not in self._rules_set:
            self._rules_set.add('invariant')
            self.rules.append('invariant')
        return KerMLTransTemplate.invariant(self, tree)

    @v_args(tree=True)
    def invariant_bool(self, tree: Tree):
        if 'invariant_bool' not in self._rules_set:
            self._rules_set.add('invariant_bool')
            self.rules.append('invariant_bool')
        return KerMLTransTemplate.invariant_bool(self, tree)

    @v_args(tree=True)
    def conditional_expression(self, tree: Tree):
        if 'conditional_expression' not in self._rules_set:
            self._rules_set.add('conditional_expression')
            self.rules.append('conditional_expression')
        return KerMLTransTemplate.conditional_expression(self, tree)

    @v_args(tree=True)
    def conditional_binary_l14_operator_expression(self, tree: Tree):
        if 'conditional_binary_l14_operator_expression' not in self._rules_set:
            self._rules_set.add('conditional_binary_l14_operator_expression')
            self.rules.append('conditional_binary_l14_operator_expression')
        return KerMLTransTemplate.conditional_binary_l14_operator_expression(self, tree)

    @v_args(tree=True)
    def conditional_binary_l14_operator(self, tree: Tree):
        if 'conditional_binary_l14_operator' not in self._rules_set:
            self._rules_set.add('conditional_binary_l14_operator')
            self.rules.append('conditional_binary_l14_operator')
        return KerMLTransTemplate.conditional_binary_l14_operator(self, tree)

    @v_args(tree=True)
    def conditional_binary_l13_operator_expression(self, tree: Tree):
        if 'conditional_binary_l13_operator_expression' not in self._rules_set:
            self._rules_set.add('conditional_binary_l13_operator_expression')
            self.rules.append('conditional_binary_l13_operator_expression')
        return KerMLTransTemplate.conditional_binary_l13_operator_expression(self, tree)

    @v_args(tree=True)
    def conditional_binary_l13_operator(self, tree: Tree):
        if 'conditional_binary_l13_operator' not in self._rules_set:
            self._rules_set.add('conditional_binary_l13_operator')
            self.rules.append('conditional_binary_l13_operator')
        return KerMLTransTemplate.conditional_binary_l13_operator(self, tree)

    @v_args(tree=True)
    def conditional_binary_l12_operator_expression(self, tree: Tree):
        if 'conditional_binary_l12_operator_expression' not in self._rules_set:
            self._rules_set.add('conditional_binary_l12_operator_expression')
            self.rules.append('conditional_binary_l12_operator_expression')
        return KerMLTransTemplate.conditional_binary_l12_operator_expression(self, tree)

    @v_args(tree=True)
    def conditional_binary_l12_operator(self, tree: Tree):
        if 'conditional_binary_l12_operator' not in self._rules_set:
            self._rules_set.add('conditional_binary_l12_operator')
            self.rules.append('conditional_binary_l12_operator')
        return KerMLTransTemplate.conditional_binary_l12_operator(self, tree)

    @v_args(tree=True)
    def binary_l12_operator_expression(self, tree: Tree):
        if 'binary_l12_operator_expression' not in self._rules_set:
            self._rules_set.add('binary_l12_operator_expression')
            self.rules.append('binary_l12_operator_expression')
        return KerMLTransTemplate.binary_l12_operator_expression(self, tree)

    @v_args(tree=True)
    def binary_l12_operator(self, tree: Tree):
        if 'binary_l12_operator' not in self._rules_set:
            self._rules_set.add('binary_l12_operator')
            self.rules.append('binary_l12_operator')
        return KerMLTransTemplate.binary_l12_operator(self, tree)

    @v_args(tree=True)
    def binary_l11_operator_expression(self, tree: Tree):
        if 'binary_l11_operator_expression' not in self._rules_set:
            self._rules_set.add('binary_l11_operator_expression')
            self.rules.append('binary_l11_operator_expression')
        return KerMLTransTemplate.binary_l11_operator_expression(self, tree)

    @v_args(tree=True)
    def binary_l11_operator(self, tree: Tree):
        if 'binary_l11_operator' not in self._rules_set:
            self._rules_set.add('binary_l11_operator')
            self.rules.append('binary_l11_operator')
        return KerMLTransTemplate.binary_l11_operator(self, tree)

    @v_args(tree=True)
    def conditional_binary_l10_operator_expression(self, tree: Tree):
        if 'conditional_binary_l10_operator_expression' not in self._rules_set:
            self._rules_set.add('conditional_binary_l10_operator_expression')
            self.rules.append('conditional_binary_l10_operator_expression')
        return KerMLTransTemplate.conditional_binary_l10_operator_expression(self, tree)

    @v_args(tree=True)
    def conditional_binary_l10_operator(self, tree: Tree):
        if 'conditional_binary_l10_operator' not in self._rules_set:
            self._rules_set.add('conditional_binary_l10_operator')
            self.rules.append('conditional_binary_l10_operator')
        return KerMLTransTemplate.conditional_binary_l10_operator(self, tree)

    @v_args(tree=True)
    def binary_l10_operator_expression(self, tree: Tree):
        if 'binary_l10_operator_expression' not in self._rules_set:
            self._rules_set.add('binary_l10_operator_expression')
            self.rules.append('binary_l10_operator_expression')
        return KerMLTransTemplate.binary_l10_operator_expression(self, tree)

    @v_args(tree=True)
    def binary_l10_operator(self, tree: Tree):
        if 'binary_l10_operator' not in self._rules_set:
            self._rules_set.add('binary_l10_operator')
            self.rules.append('binary_l10_operator')
        return KerMLTransTemplate.binary_l10_operator(self, tree)

    @v_args(tree=True)
    def binary_l9_operator_expression(self, tree: Tree):
        if 'binary_l9_operator_expression' not in self._rules_set:
            self._rules_set.add('binary_l9_operator_expression')
            self.rules.append('binary_l9_operator_expression')
        return KerMLTransTemplate.binary_l9_operator_expression(self, tree)

    @v_args(tree=True)
    def binary_l9_operator(self, tree: Tree):
        if 'binary_l9_operator' not in self._rules_set:
            self._rules_set.add('binary_l9_operator')
            self.rules.append('binary_l9_operator')
        return KerMLTransTemplate.binary_l9_operator(self, tree)

    @v_args(tree=True)
    def classification_expression(self, tree: Tree):
        if 'classification_expression' not in self._rules_set:
            self._rules_set.add('classification_expression')
            self.rules.append('classification_expression')
        return KerMLTransTemplate.classification_expression(self, tree)

    @v_args(tree=True)
    def classification_test_operator(self, tree: Tree):
        if 'classification_test_operator' not in self._rules_set:
            self._rules_set.add('classification_test_operator')
            self.rules.append('classification_test_operator')
        return KerMLTransTemplate.classification_test_operator(self, tree)

    @v_args(tree=True)
    def cast_operator(self, tree: Tree):
        if 'cast_operator' not in self._rules_set:
            self._rules_set.add('cast_operator')
            self.rules.append('cast_operator')
        return KerMLTransTemplate.cast_operator(self, tree)

    @v_args(tree=True)
    def metaclassification_expression(self, tree: Tree):
        if 'metaclassification_expression' not in self._rules_set:
            self._rules_set.add('metaclassification_expression')
            self.rules.append('metaclassification_expression')
        return KerMLTransTemplate.metaclassification_expression(self, tree)

    @v_args(tree=True)
    def meta_classification_test_operator(self, tree: Tree):
        if 'meta_classification_test_operator' not in self._rules_set:
            self._rules_set.add('meta_classification_test_operator')
            self.rules.append('meta_classification_test_operator')
        return KerMLTransTemplate.meta_classification_test_operator(self, tree)

    @v_args(tree=True)
    def meta_cast_operator(self, tree: Tree):
        if 'meta_cast_operator' not in self._rules_set:
            self._rules_set.add('meta_cast_operator')
            self.rules.append('meta_cast_operator')
        return KerMLTransTemplate.meta_cast_operator(self, tree)

    @v_args(tree=True)
    def binary_l7_operator_expression(self, tree: Tree):
        if 'binary_l7_operator_expression' not in self._rules_set:
            self._rules_set.add('binary_l7_operator_expression')
            self.rules.append('binary_l7_operator_expression')
        return KerMLTransTemplate.binary_l7_operator_expression(self, tree)

    @v_args(tree=True)
    def binary_l7_operator(self, tree: Tree):
        if 'binary_l7_operator' not in self._rules_set:
            self._rules_set.add('binary_l7_operator')
            self.rules.append('binary_l7_operator')
        return KerMLTransTemplate.binary_l7_operator(self, tree)

    @v_args(tree=True)
    def binary_l6_operator_expression(self, tree: Tree):
        if 'binary_l6_operator_expression' not in self._rules_set:
            self._rules_set.add('binary_l6_operator_expression')
            self.rules.append('binary_l6_operator_expression')
        return KerMLTransTemplate.binary_l6_operator_expression(self, tree)

    @v_args(tree=True)
    def binary_l6_operator(self, tree: Tree):
        if 'binary_l6_operator' not in self._rules_set:
            self._rules_set.add('binary_l6_operator')
            self.rules.append('binary_l6_operator')
        return KerMLTransTemplate.binary_l6_operator(self, tree)

    @v_args(tree=True)
    def binary_l5_operator_expression(self, tree: Tree):
        if 'binary_l5_operator_expression' not in self._rules_set:
            self._rules_set.add('binary_l5_operator_expression')
            self.rules.append('binary_l5_operator_expression')
        return KerMLTransTemplate.binary_l5_operator_expression(self, tree)

    @v_args(tree=True)
    def binary_l5_operator(self, tree: Tree):
        if 'binary_l5_operator' not in self._rules_set:
            self._rules_set.add('binary_l5_operator')
            self.rules.append('binary_l5_operator')
        return KerMLTransTemplate.binary_l5_operator(self, tree)

    @v_args(tree=True)
    def binary_l4_operator_expression(self, tree: Tree):
        if 'binary_l4_operator_expression' not in self._rules_set:
            self._rules_set.add('binary_l4_operator_expression')
            self.rules.append('binary_l4_operator_expression')
        return KerMLTransTemplate.binary_l4_operator_expression(self, tree)

    @v_args(tree=True)
    def binary_l4_operator(self, tree: Tree):
        if 'binary_l4_operator' not in self._rules_set:
            self._rules_set.add('binary_l4_operator')
            self.rules.append('binary_l4_operator')
        return KerMLTransTemplate.binary_l4_operator(self, tree)

    @v_args(tree=True)
    def exp_operator_expression(self, tree: Tree):
        if 'exp_operator_expression' not in self._rules_set:
            self._rules_set.add('exp_operator_expression')
            self.rules.append('exp_operator_expression')
        return KerMLTransTemplate.exp_operator_expression(self, tree)

    @v_args(tree=True)
    def unary_operator_expression(self, tree: Tree):
        if 'unary_operator_expression' not in self._rules_set:
            self._rules_set.add('unary_operator_expression')
            self.rules.append('unary_operator_expression')
        return KerMLTransTemplate.unary_operator_expression(self, tree)

    @v_args(tree=True)
    def unary_operator(self, tree: Tree):
        if 'unary_operator' not in self._rules_set:
            self._rules_set.add('unary_operator')
            self.rules.append('unary_operator')
        return KerMLTransTemplate.unary_operator(self, tree)

    @v_args(tree=True)
    def extent_expression(self, tree: Tree):
        if 'extent_expression' not in self._rules_set:
            self._rules_set.add('extent_expression')
            self.rules.append('extent_expression')
        return KerMLTransTemplate.extent_expression(self, tree)

    @v_args(tree=True)
    def bracket_expression(self, tree: Tree):
        if 'bracket_expression' not in self._rules_set:
            self._rules_set.add('bracket_expression')
            self.rules.append('bracket_expression')
        return KerMLTransTemplate.bracket_expression(self, tree)

    @v_args(tree=True)
    def index_expression(self, tree: Tree):
        if 'index_expression' not in self._rules_set:
            self._rules_set.add('index_expression')
            self.rules.append('index_expression')
        return KerMLTransTemplate.index_expression(self, tree)

    @v_args(tree=True)
    def sequence_expression(self, tree: Tree):
        if 'sequence_expression' not in self._rules_set:
            self._rules_set.add('sequence_expression')
            self.rules.append('sequence_expression')
        return KerMLTransTemplate.sequence_expression(self, tree)

    @v_args(tree=True)
    def sequence_operator_expression(self, tree: Tree):
        if 'sequence_operator_expression' not in self._rules_set:
            self._rules_set.add('sequence_operator_expression')
            self.rules.append('sequence_operator_expression')
        return KerMLTransTemplate.sequence_operator_expression(self, tree)

    @v_args(tree=True)
    def feature_chain_expression(self, tree: Tree):
        if 'feature_chain_expression' not in self._rules_set:
            self._rules_set.add('feature_chain_expression')
            self.rules.append('feature_chain_expression')
        return KerMLTransTemplate.feature_chain_expression(self, tree)

    @v_args(tree=True)
    def collect_expression(self, tree: Tree):
        if 'collect_expression' not in self._rules_set:
            self._rules_set.add('collect_expression')
            self.rules.append('collect_expression')
        return KerMLTransTemplate.collect_expression(self, tree)

    @v_args(tree=True)
    def select_expression(self, tree: Tree):
        if 'select_expression' not in self._rules_set:
            self._rules_set.add('select_expression')
            self.rules.append('select_expression')
        return KerMLTransTemplate.select_expression(self, tree)

    @v_args(tree=True)
    def null_expression(self, tree: Tree):
        if 'null_expression' not in self._rules_set:
            self._rules_set.add('null_expression')
            self.rules.append('null_expression')
        return KerMLTransTemplate.null_expression(self, tree)

    @v_args(tree=True)
    def metadata_access_expression(self, tree: Tree):
        if 'metadata_access_expression' not in self._rules_set:
            self._rules_set.add('metadata_access_expression')
            self.rules.append('metadata_access_expression')
        return KerMLTransTemplate.metadata_access_expression(self, tree)

    @v_args(tree=True)
    def invocation_expression(self, tree: Tree):
        if 'invocation_expression' not in self._rules_set:
            self._rules_set.add('invocation_expression')
            self.rules.append('invocation_expression')
        return KerMLTransTemplate.invocation_expression(self, tree)

    @v_args(tree=True)
    def argument_list(self, tree: Tree):
        if 'argument_list' not in self._rules_set:
            self._rules_set.add('argument_list')
            self.rules.append('argument_list')
        return KerMLTransTemplate.argument_list(self, tree)

    @v_args(tree=True)
    def positional_argument_list(self, tree: Tree):
        if 'positional_argument_list' not in self._rules_set:
            self._rules_set.add('positional_argument_list')
            self.rules.append('positional_argument_list')
        return KerMLTransTemplate.positional_argument_list(self, tree)

    @v_args(tree=True)
    def named_argument_list(self, tree: Tree):
        if 'named_argument_list' not in self._rules_set:
            self._rules_set.add('named_argument_list')
            self.rules.append('named_argument_list')
        return KerMLTransTemplate.named_argument_list(self, tree)

    @v_args(tree=True)
    def named_argument(self, tree: Tree):
        if 'named_argument' not in self._rules_set:
            self._rules_set.add('named_argument')
            self.rules.append('named_argument')
        return KerMLTransTemplate.named_argument(self, tree)

    @v_args(tree=True)
    def body_expression(self, tree: Tree):
        if 'body_expression' not in self._rules_set:
            self._rules_set.add('body_expression')
            self.rules.append('body_expression')
        return KerMLTransTemplate.body_expression(self, tree)

    @v_args(tree=True)
    def expression_body(self, tree: Tree):
        if 'expression_body' not in self._rules_set:
            self._rules_set.add('expression_body')
            self.rules.append('expression_body')
        return KerMLTransTemplate.expression_body(self, tree)

    @v_args(tree=True)
    def literal_boolean(self, tree: Tree):
        if 'literal_boolean' not in self._rules_set:
            self._rules_set.add('literal_boolean')
            self.rules.append('literal_boolean')
        return KerMLTransTemplate.literal_boolean(self, tree)

    @v_args(tree=True)
    def literal_string(self, tree: Tree):
        if 'literal_string' not in self._rules_set:
            self._rules_set.add('literal_string')
            self.rules.append('literal_string')
        return KerMLTransTemplate.literal_string(self, tree)

    @v_args(tree=True)
    def literal_integer(self, tree: Tree):
        if 'literal_integer' not in self._rules_set:
            self._rules_set.add('literal_integer')
            self.rules.append('literal_integer')
        return KerMLTransTemplate.literal_integer(self, tree)

    @v_args(tree=True)
    def literal_real(self, tree: Tree):
        if 'literal_real' not in self._rules_set:
            self._rules_set.add('literal_real')
            self.rules.append('literal_real')
        return KerMLTransTemplate.literal_real(self, tree)

    @v_args(tree=True)
    def literal_infinity(self, tree: Tree):
        if 'literal_infinity' not in self._rules_set:
            self._rules_set.add('literal_infinity')
            self.rules.append('literal_infinity')
        return KerMLTransTemplate.literal_infinity(self, tree)

    @v_args(tree=True)
    def interaction(self, tree: Tree):
        if 'interaction' not in self._rules_set:
            self._rules_set.add('interaction')
            self.rules.append('interaction')
        return KerMLTransTemplate.interaction(self, tree)

    @v_args(tree=True)
    def item_flow(self, tree: Tree):
        if 'item_flow' not in self._rules_set:
            self._rules_set.add('item_flow')
            self.rules.append('item_flow')
        return KerMLTransTemplate.item_flow(self, tree)

    @v_args(tree=True)
    def succession_item_flow(self, tree: Tree):
        if 'succession_item_flow' not in self._rules_set:
            self._rules_set.add('succession_item_flow')
            self.rules.append('succession_item_flow')
        return KerMLTransTemplate.succession_item_flow(self, tree)

    @v_args(tree=True)
    def item_feature_specialization_part(self, tree: Tree):
        if 'item_feature_specialization_part' not in self._rules_set:
            self._rules_set.add('item_feature_specialization_part')
            self.rules.append('item_feature_specialization_part')
        return KerMLTransTemplate.item_feature_specialization_part(self, tree)

    @v_args(tree=True)
    def item_flow_end(self, tree: Tree):
        if 'item_flow_end' not in self._rules_set:
            self._rules_set.add('item_flow_end')
            self.rules.append('item_flow_end')
        return KerMLTransTemplate.item_flow_end(self, tree)

    @v_args(tree=True)
    def feature_value(self, tree: Tree):
        if 'feature_value' not in self._rules_set:
            self._rules_set.add('feature_value')
            self.rules.append('feature_value')
        return KerMLTransTemplate.feature_value(self, tree)

    @v_args(tree=True)
    def multiplicity_subset(self, tree: Tree):
        if 'multiplicity_subset' not in self._rules_set:
            self._rules_set.add('multiplicity_subset')
            self.rules.append('multiplicity_subset')
        return KerMLTransTemplate.multiplicity_subset(self, tree)

    @v_args(tree=True)
    def multiplicity_range(self, tree: Tree):
        if 'multiplicity_range' not in self._rules_set:
            self._rules_set.add('multiplicity_range')
            self.rules.append('multiplicity_range')
        return KerMLTransTemplate.multiplicity_range(self, tree)

    @v_args(tree=True)
    def multiplicity_bounds(self, tree: Tree):
        if 'multiplicity_bounds' not in self._rules_set:
            self._rules_set.add('multiplicity_bounds')
            self.rules.append('multiplicity_bounds')
        return KerMLTransTemplate.multiplicity_bounds(self, tree)

    @v_args(tree=True)
    def metaclass(self, tree: Tree):
        if 'metaclass' not in self._rules_set:
            self._rules_set.add('metaclass')
            self.rules.append('metaclass')
        return KerMLTransTemplate.metaclass(self, tree)

    @v_args(tree=True)
    def prefix_metadata_annotation(self, tree: Tree):
        if 'prefix_metadata_annotation' not in self._rules_set:
            self._rules_set.add('prefix_metadata_annotation')
            self.rules.append('prefix_metadata_annotation')
        return KerMLTransTemplate.prefix_metadata_annotation(self, tree)

    @v_args(tree=True)
    def prefix_metadata_member(self, tree: Tree):
        if 'prefix_metadata_member' not in self._rules_set:
            self._rules_set.add('prefix_metadata_member')
            self.rules.append('prefix_metadata_member')
        return KerMLTransTemplate.prefix_metadata_member(self, tree)

    @v_args(tree=True)
    def metadata_feature(self, tree: Tree):
        if 'metadata_feature' not in self._rules_set:
            self._rules_set.add('metadata_feature')
            self.rules.append('metadata_feature')
        return KerMLTransTemplate.metadata_feature(self, tree)

    @v_args(tree=True)
    def metadata_feature_about(self, tree: Tree):
        if 'metadata_feature_about' not in self._rules_set:
            self._rules_set.add('metadata_feature_about')
            self.rules.append('metadata_feature_about')
        return KerMLTransTemplate.metadata_feature_about(self, tree)

    @v_args(tree=True)
    def metadata_feature_declaration(self, tree: Tree):
        if 'metadata_feature_declaration' not in self._rules_set:
            self._rules_set.add('metadata_feature_declaration')
            self.rules.append('metadata_feature_declaration')
        return KerMLTransTemplate.metadata_feature_declaration(self, tree)

    @v_args(tree=True)
    def metadata_body(self, tree: Tree):
        if 'metadata_body' not in self._rules_set:
            self._rules_set.add('metadata_body')
            self.rules.append('metadata_body')
        return KerMLTransTemplate.metadata_body(self, tree)

    @v_args(tree=True)
    def metadata_body_feature(self, tree: Tree):
        if 'metadata_body_feature' not in self._rules_set:
            self._rules_set.add('metadata_body_feature')
            self.rules.append('metadata_body_feature')
        return KerMLTransTemplate.metadata_body_feature(self, tree)

    @v_args(tree=True)
    def package(self, tree: Tree):
        if 'package' not in self._rules_set:
            self._rules_set.add('package')
            self.rules.append('package')
        return KerMLTransTemplate.package(self, tree)

    @v_args(tree=True)
    def library_package(self, tree: Tree):
        if 'library_package' not in self._rules_set:
            self._rules_set.add('library_package')
            self.rules.append('library_package')
        return KerMLTransTemplate.library_package(self, tree)

    @v_args(tree=True)
    def package_declaration(self, tree: Tree):
        if 'package_declaration' not in self._rules_set:
            self._rules_set.add('package_declaration')
            self.rules.append('package_declaration')
        return KerMLTransTemplate.package_declaration(self, tree)

    @v_args(tree=True)
    def package_body(self, tree: Tree):
        if 'package_body' not in self._rules_set:
            self._rules_set.add('package_body')
            self.rules.append('package_body')
        return KerMLTransTemplate.package_body(self, tree)

    @v_args(tree=True)
    def element_filter_member(self, tree: Tree):
        if 'element_filter_member' not in self._rules_set:
            self._rules_set.add('element_filter_member')
            self.rules.append('element_filter_member')
        return KerMLTransTemplate.element_filter_member(self, tree)

