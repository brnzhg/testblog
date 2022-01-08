from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import nested_parse_with_titles

import os

from sphinx.util import logging


logger = logging.getLogger(__name__)




# TODO this will be fancy class that interprets options to know which files to generate, and which env variables to populate
# class is created at beginning, from options
def test_include_register_builder_inited(app):
    env = app.builder.env

    # if not hasattr(env, 'todo_all_todos'):
    env.test_include_test_data = { 
        'bob': 'pizza',
        'george': 'burger'
        }
    

class TestInclude(SphinxDirective):

    # this enables content in the directive
    has_content = True

    def run(self):

        
        include_node = nodes.paragraph()

        docpath = self.env.doc2path(self.env.docname)

        dirname = os.path.dirname(docpath)
        include_filepath = os.path.join(dirname, 'toinclude.rst') # TODO this should be a parameter from the directive
        try:
            
            print(include_filepath)
            logger.info(include_filepath)

        
            with open(include_filepath, 'r') as f:
                include_contents = [l for l in f]

            
            print(include_contents)

            #self.state.nested_parse_incldue(include_contents, self.content_offset, include_node)
            nested_parse_with_titles(self.state, include_contents, include_node)
        except:
            pass


        print('cool')
        bob_node = nodes.paragraph(text='bob likes ' + self.env.test_include_test_data['bob'] + ' ' + include_filepath)

        # return [bob_node, include_node]
        return [bob_node, include_node]


def setup(app):
    # app.add_config_value('todo_include_todos', False, 'html')

    app.add_directive('testinclude', TestInclude)
    app.connect('builder-inited', test_include_register_builder_inited)
    # app.connect('doctree-resolved', process_todo_nodes)
    # app.connect('env-purge-doc', purge_todos)
    # app.connect('env-merge-info', merge_todos)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
