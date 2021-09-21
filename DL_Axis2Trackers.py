# --------------------------------------------------------------
#  DL_Axis2Trackers.py
#  Version: v01.1
#  Author: Danilo de Lucio
#
#  Last Modified by: Danilo de Lucio
#  Last Updated: August 02th, 2021
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Convert multiples Axis nodes to 2D Trackers.
# --------------------------------------------------------------


# Fazer o código funcionar apenas com Axis selecionados
for i in nuke.selectedNodes("Axis2"):
    # Pegar o nome de cada Axis selecionado
    axis_selection = i["name"].getValue()

    # Conectar o Input do Reconcile no Axis selecionado
    reconcile = nuke.toNode("Reconcile3D2")
    reconcile.setInput(2, nuke.toNode(axis_selection))

    # Executar o botão "create_keyframes"
    nuke.execute(reconcile)

    # Guardar os valores de X e Y do knob "output"
    reconcile_output = reconcile["output"].getValue()

    rec_output_x = reconcile_output[0]
    rec_output_y = reconcile_output[1]

    print(rec_output_x)
    print(rec_output_y)

    # Criar um Tracker node
    tracker = nuke.createNode("Tracker4")
    tracker["add_tracker"].execute()
