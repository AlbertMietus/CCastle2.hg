DEMO (1)
========

.. seealso:: https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#space-separated-format

ReStructuredText example
------------------------

This text is outside code blocks and thus ignored.

.. code:: robotframework

   *** Settings ***
   Documentation    Example using the reStructuredText format.
   Library          OperatingSystem

   *** Variables ***
   ${MESSAGE}       Hello, world!

   *** Test Cases ***
   My Test
       [Documentation]    Example test.
       Log    ${MESSAGE}
       My Keyword    ${CURDIR}

   Another Test
       Should Be Equal    ${MESSAGE}    Hello, world!

Also this text is outside code blocks and ignored. Code blocks not
containing Robot Framework data are ignored as well.

.. code:: robotframework

   # Both space and pipe separated formats are supported.

   | *** Keywords ***  |                        |         |
   | My Keyword        | [Arguments]            | ${path} |
   |                   | Directory Should Exist | ${path} |

.. code:: python

   # This code block is ignored.
   def example():
       print('Hello, world!')


With INCLUEDED .Robot file (`demo1.robot`)
------------------------------------------

.. literalinclude:: demo1.robot
   :language:  robotframework

.. note::

   * the :file:`demo1.robot` contains the same code as the (top) above example
   * Now, however, that test is syntax-highlighted (in emacs) -- in html it is the same
   * See https://github.com/kopoli/robot-mode -- it is manually downloaded in ~/emacs/



Embedded arguments (`demo2.robot`)
----------------------------------

.. literalinclude:: demo2.robot
   :language:  robotframework

.. note::

   * A user-keyword with an embedded arguments/parameter is not (correctly/blue)highlighted in emacs
   * But it is in rst/sphinx/pygymentize
