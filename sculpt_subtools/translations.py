"""Traducciones del addon Sculpt Subtools (bpy.app.translations).

Los msgids son los textos en inglés del código (idioma base). Blender elige
el idioma según la preferencia de idioma, por defecto "Automático" (sistema).
"""

import bpy

_LOCALES = ("es", "fr_FR", "de_DE", "zh_HANS", "ja_JP", "ko_KR", "pt_BR", "it_IT")

_ALIASES = {"es_ES": "es", "zh_CN": "zh_HANS", "pt_PT": "pt_BR"}

_CONTEXTS = ("*", "Operator")

# msgid (inglés) → (es, fr, de, zh-Hans, ja, ko, pt, it)
_STRINGS = {
    # --- Panel ---
    "Select a mesh": (
        "Selecciona una malla",
        "Sélectionnez un maillage",
        "Wähle ein Mesh aus",
        "请选择一个网格",
        "メッシュを選択してください",
        "메시를 선택하세요",
        "Selecione uma malha",
        "Seleziona una mesh",
    ),
    "Add": (
        "Añadir", "Ajouter", "Hinzufügen", "添加",
        "追加", "추가", "Adicionar", "Aggiungi",
    ),
    "Mirror": (
        "Espejar", "Miroir", "Spiegeln", "镜像",
        "ミラー", "미러", "Espelhar", "Specchia",
    ),
    "Duplicate": (
        "Duplicar", "Dupliquer", "Duplizieren", "复制",
        "複製", "복제", "Duplicar", "Duplica",
    ),
    "Delete": (
        "Borrar", "Supprimer", "Löschen", "删除",
        "削除", "삭제", "Apagar", "Elimina",
    ),
    "Up": (
        "Subir", "Monter", "Nach oben", "上移",
        "上へ", "위로", "Subir", "Su",
    ),
    "Down": (
        "Bajar", "Descendre", "Nach unten", "下移",
        "下へ", "아래로", "Descer", "Giù",
    ),
    "Merge": (
        "Unir", "Fusionner", "Vereinen", "合并",
        "統合", "합치기", "Unir", "Unisci",
    ),
    "Split into subtools:": (
        "Separar en subtools:",
        "Séparer en subtools :",
        "In Subtools aufteilen:",
        "拆分为子工具：",
        "サブツールに分割:",
        "서브툴로 분리:",
        "Separar em subtools:",
        "Separa in subtool:",
    ),
    "Loose Parts": (
        "Sueltas", "Parties isolées", "Lose Teile", "松散块",
        "分離パーツ", "분리된 부분", "Partes soltas", "Parti separate",
    ),
    "Mask": (
        "Máscara", "Masque", "Maske", "遮罩",
        "マスク", "마스크", "Máscara", "Maschera",
    ),
    "Show All": (
        "Mostrar todo", "Tout afficher", "Alle anzeigen", "全部显示",
        "すべて表示", "모두 표시", "Mostrar tudo", "Mostra tutto",
    ),
    "Frame": (
        "Enmarcar", "Cadrer", "Einrahmen", "框显",
        "フレーム表示", "화면에 맞추기", "Enquadrar", "Inquadra",
    ),
    "Boolean": (
        "Booleana", "Booléen", "Boolesch", "布尔",
        "ブーリアン", "불리언", "Booleana", "Booleana",
    ),
    "Union": (
        "Unión", "Union", "Vereinigung", "并集",
        "合成", "합집합", "União", "Unione",
    ),
    "Difference": (
        "Resta", "Différence", "Differenz", "差集",
        "差分", "차집합", "Diferença", "Differenza",
    ),
    "Intersect": (
        "Insec.", "Intersection", "Schnitt", "交集",
        "交差", "교집합", "Interseção", "Interseca",
    ),
    "Remove Preview": (
        "Quitar preview", "Retirer l'aperçu", "Vorschau entfernen", "移除预览",
        "プレビューを解除", "미리보기 제거", "Remover preview", "Rimuovi anteprima",
    ),
    "Live Preview": (
        "Preview en vivo", "Aperçu en direct", "Live-Vorschau", "实时预览",
        "ライブプレビュー", "실시간 미리보기", "Preview ao vivo", "Anteprima live",
    ),
    "Apply Boolean": (
        "Aplicar booleana", "Appliquer le booléen", "Boolean anwenden", "应用布尔",
        "ブーリアンを適用", "불리언 적용", "Aplicar booleana", "Applica booleana",
    ),
    "{} subtools · {} ({} faces)": (
        "{} subtools · {} ({} caras)",
        "{} subtools · {} ({} faces)",
        "{} Subtools · {} ({} Flächen)",
        "{} 个子工具 · {}（{} 面）",
        "{} サブツール · {}（{} 面）",
        "서브툴 {}개 · {} (면 {}개)",
        "{} subtools · {} ({} faces)",
        "{} subtool · {} ({} facce)",
    ),
    # --- Operadores: labels y tooltips ---
    "Activate Subtool": (
        "Activar subtool", "Activer le subtool", "Subtool aktivieren", "激活子工具",
        "サブツールをアクティブ化", "서브툴 활성화", "Ativar subtool", "Attiva subtool",
    ),
    "Makes this subtool active (jumps to it without leaving Sculpt)": (
        "Hace activo este subtool (salta a él sin salir de Sculpt)",
        "Rend ce subtool actif (bascule dessus sans quitter le mode Sculpt)",
        "Macht dieses Subtool aktiv (wechselt dorthin, ohne Sculpt zu verlassen)",
        "激活此子工具（无需退出雕刻模式即可切换）",
        "このサブツールをアクティブにします（スカルプトを離れずに切り替え）",
        "이 서브툴을 활성화합니다 (스컬프트를 벗어나지 않고 이동)",
        "Torna este subtool ativo (salta para ele sem sair do Sculpt)",
        "Rende attivo questo subtool (ci passa senza uscire da Sculpt)",
    ),
    "Cycle Subtool": (
        "Ciclar subtool", "Parcourir les subtools", "Subtool wechseln", "循环切换子工具",
        "サブツールを切り替え", "서브툴 순환", "Alternar subtool", "Cicla subtool",
    ),
    "Jumps to the previous or next subtool of the active Tool": (
        "Salta al subtool anterior o siguiente del Tool activo",
        "Passe au subtool précédent ou suivant du Tool actif",
        "Springt zum vorherigen oder nächsten Subtool des aktiven Tools",
        "跳转到当前 Tool 的上一个或下一个子工具",
        "アクティブな Tool の前後のサブツールに移動します",
        "활성 Tool의 이전 또는 다음 서브툴로 이동합니다",
        "Salta para o subtool anterior ou seguinte do Tool ativo",
        "Passa al subtool precedente o successivo del Tool attivo",
    ),
    "Previous": (
        "Anterior", "Précédent", "Vorheriges", "上一个",
        "前へ", "이전", "Anterior", "Precedente",
    ),
    "Previous subtool": (
        "Subtool anterior", "Subtool précédent", "Vorheriges Subtool", "上一个子工具",
        "前のサブツール", "이전 서브툴", "Subtool anterior", "Subtool precedente",
    ),
    "Next": (
        "Siguiente", "Suivant", "Nächstes", "下一个",
        "次へ", "다음", "Seguinte", "Successivo",
    ),
    "Next subtool": (
        "Subtool siguiente", "Subtool suivant", "Nächstes Subtool", "下一个子工具",
        "次のサブツール", "다음 서브툴", "Subtool seguinte", "Subtool successivo",
    ),
    "Subtool Visibility": (
        "Visibilidad del subtool", "Visibilité du subtool", "Subtool-Sichtbarkeit",
        "子工具可见性", "サブツールの表示", "서브툴 표시 여부",
        "Visibilidade do subtool", "Visibilità del subtool",
    ),
    "Shows or hides this subtool": (
        "Muestra u oculta este subtool",
        "Affiche ou masque ce subtool",
        "Zeigt oder verbirgt dieses Subtool",
        "显示或隐藏此子工具",
        "このサブツールを表示・非表示にします",
        "이 서브툴을 표시하거나 숨깁니다",
        "Mostra ou oculta este subtool",
        "Mostra o nasconde questo subtool",
    ),
    "Solo": (
        "Solo", "Solo", "Solo", "独显",
        "ソロ", "솔로", "Solo", "Solo",
    ),
    "Isolates this subtool by hiding the rest (toggle)": (
        "Aísla este subtool ocultando el resto (toggle)",
        "Isole ce subtool en masquant les autres (bascule)",
        "Isoliert dieses Subtool und verbirgt die übrigen (Umschalter)",
        "隔离此子工具并隐藏其余（切换）",
        "他を隠してこのサブツールを分離表示します（トグル）",
        "나머지를 숨겨 이 서브툴만 표시합니다 (토글)",
        "Isola este subtool ocultando os demais (alternar)",
        "Isola questo subtool nascondendo gli altri (interruttore)",
    ),
    "Duplicate Subtool": (
        "Duplicar subtool", "Dupliquer le subtool", "Subtool duplizieren", "复制子工具",
        "サブツールを複製", "서브툴 복제", "Duplicar subtool", "Duplica subtool",
    ),
    "Duplicates the active subtool": (
        "Duplica el subtool activo",
        "Duplique le subtool actif",
        "Dupliziert das aktive Subtool",
        "复制当前子工具",
        "アクティブなサブツールを複製します",
        "활성 서브툴을 복제합니다",
        "Duplica o subtool ativo",
        "Duplica il subtool attivo",
    ),
    "Delete Subtool": (
        "Borrar subtool", "Supprimer le subtool", "Subtool löschen", "删除子工具",
        "サブツールを削除", "서브툴 삭제", "Apagar subtool", "Elimina subtool",
    ),
    "Deletes the active subtool": (
        "Borra el subtool activo",
        "Supprime le subtool actif",
        "Löscht das aktive Subtool",
        "删除当前子工具",
        "アクティブなサブツールを削除します",
        "활성 서브툴을 삭제합니다",
        "Apaga o subtool ativo",
        "Elimina il subtool attivo",
    ),
    "Move Subtool": (
        "Mover subtool", "Déplacer le subtool", "Subtool verschieben", "移动子工具",
        "サブツールを移動", "서브툴 이동", "Mover subtool", "Sposta subtool",
    ),
    "Moves the active subtool up or down within its group": (
        "Sube o baja el subtool activo en su grupo",
        "Monte ou descend le subtool actif dans son groupe",
        "Verschiebt das aktive Subtool in seiner Gruppe nach oben oder unten",
        "在组内上移或下移当前子工具",
        "アクティブなサブツールをグループ内で上下に移動します",
        "활성 서브툴을 그룹 안에서 위아래로 이동합니다",
        "Sobe ou desce o subtool ativo no seu grupo",
        "Sposta su o giù il subtool attivo nel suo gruppo",
    ),
    "Move up": (
        "Mover arriba", "Monter", "Nach oben verschieben", "上移",
        "上へ移動", "위로 이동", "Mover para cima", "Sposta su",
    ),
    "Move down": (
        "Mover abajo", "Descendre", "Nach unten verschieben", "下移",
        "下へ移動", "아래로 이동", "Mover para baixo", "Sposta giù",
    ),
    "New Group": (
        "Nuevo grupo", "Nouveau groupe", "Neue Gruppe", "新建组",
        "新規グループ", "새 그룹", "Novo grupo", "Nuovo gruppo",
    ),
    "Creates a group (sub-collection) inside the active Tool": (
        "Crea un grupo (sub-colección) dentro del Tool activo",
        "Crée un groupe (sous-collection) dans le Tool actif",
        "Erstellt eine Gruppe (Untersammlung) im aktiven Tool",
        "在当前 Tool 内创建一个组（子集合）",
        "アクティブな Tool 内にグループ（サブコレクション）を作成します",
        "활성 Tool 안에 그룹(하위 컬렉션)을 만듭니다",
        "Cria um grupo (subcoleção) dentro do Tool ativo",
        "Crea un gruppo (sotto-collezione) dentro il Tool attivo",
    ),
    "Name": (
        "Nombre", "Nom", "Name", "名称",
        "名前", "이름", "Nome", "Nome",
    ),
    "Move to Group": (
        "Mover a grupo", "Déplacer vers le groupe", "In Gruppe verschieben", "移动到组",
        "グループへ移動", "그룹으로 이동", "Mover para grupo", "Sposta nel gruppo",
    ),
    "Moves the active subtool to the given group": (
        "Mueve el subtool activo al grupo indicado",
        "Déplace le subtool actif vers le groupe indiqué",
        "Verschiebt das aktive Subtool in die angegebene Gruppe",
        "将当前子工具移动到指定的组",
        "アクティブなサブツールを指定のグループへ移動します",
        "활성 서브툴을 지정한 그룹으로 이동합니다",
        "Move o subtool ativo para o grupo indicado",
        "Sposta il subtool attivo nel gruppo indicato",
    ),
    "Collapse/Expand Group": (
        "Plegar/desplegar grupo", "Plier/déplier le groupe", "Gruppe ein-/ausklappen",
        "折叠/展开组", "グループを折りたたみ／展開", "그룹 접기/펼치기",
        "Recolher/expandir grupo", "Comprimi/espandi gruppo",
    ),
    "Collapses or expands a group in the palette": (
        "Pliega o despliega un grupo en la paleta",
        "Plie ou déplie un groupe dans la palette",
        "Klappt eine Gruppe in der Palette ein oder aus",
        "在面板中折叠或展开组",
        "パレット内のグループを折りたたみ・展開します",
        "팔레트에서 그룹을 접거나 펼칩니다",
        "Recolhe ou expande um grupo na paleta",
        "Comprime o espande un gruppo nella palette",
    ),
    "Merge Subtools": (
        "Unir subtools", "Fusionner les subtools", "Subtools vereinen", "合并子工具",
        "サブツールを統合", "서브툴 합치기", "Unir subtools", "Unisci subtool",
    ),
    "Merges the selected subtools into the active one": (
        "Une los subtools seleccionados en el activo",
        "Fusionne les subtools sélectionnés dans l'actif",
        "Vereint die ausgewählten Subtools im aktiven",
        "将选中的子工具合并到当前子工具",
        "選択したサブツールをアクティブなものに統合します",
        "선택한 서브툴을 활성 서브툴에 합칩니다",
        "Une os subtools selecionados no ativo",
        "Unisce i subtool selezionati in quello attivo",
    ),
    "Split by Loose Parts": (
        "Separar por partes sueltas", "Séparer par parties isolées",
        "Nach losen Teilen aufteilen", "按松散块拆分",
        "分離パーツで分割", "분리된 부분으로 나누기",
        "Separar por partes soltas", "Separa per parti separate",
    ),
    "Splits the active subtool into its loose parts": (
        "Separa el subtool activo en sus partes sueltas",
        "Sépare le subtool actif en ses parties isolées",
        "Teilt das aktive Subtool in seine losen Teile auf",
        "将当前子工具拆分为松散块",
        "アクティブなサブツールを分離パーツごとに分割します",
        "활성 서브툴을 분리된 부분으로 나눕니다",
        "Separa o subtool ativo em suas partes soltas",
        "Separa il subtool attivo nelle sue parti separate",
    ),
    "Add Subtool": (
        "Añadir subtool", "Ajouter un subtool", "Subtool hinzufügen", "添加子工具",
        "サブツールを追加", "서브툴 추가", "Adicionar subtool", "Aggiungi subtool",
    ),
    "Adds a new primitive mesh as a subtool of the active Tool": (
        "Añade una malla primitiva nueva como subtool del Tool activo",
        "Ajoute une nouvelle primitive comme subtool du Tool actif",
        "Fügt ein neues primitives Mesh als Subtool des aktiven Tools hinzu",
        "添加一个新的基本网格作为当前 Tool 的子工具",
        "新しいプリミティブメッシュをアクティブな Tool のサブツールとして追加します",
        "새 기본 메시를 활성 Tool의 서브툴로 추가합니다",
        "Adiciona uma nova malha primitiva como subtool do Tool ativo",
        "Aggiunge una nuova mesh primitiva come subtool del Tool attivo",
    ),
    "Add a cube": (
        "Añadir un cubo", "Ajouter un cube", "Einen Würfel hinzufügen", "添加立方体",
        "立方体を追加", "큐브 추가", "Adicionar um cubo", "Aggiungi un cubo",
    ),
    "Add a sphere": (
        "Añadir una esfera", "Ajouter une sphère", "Eine Kugel hinzufügen", "添加球体",
        "球を追加", "구체 추가", "Adicionar uma esfera", "Aggiungi una sfera",
    ),
    "Add a cylinder": (
        "Añadir un cilindro", "Ajouter un cylindre", "Einen Zylinder hinzufügen",
        "添加圆柱体", "円柱を追加", "실린더 추가",
        "Adicionar um cilindro", "Aggiungi un cilindro",
    ),
    "Add a plane": (
        "Añadir un plano", "Ajouter un plan", "Eine Ebene hinzufügen", "添加平面",
        "平面を追加", "평면 추가", "Adicionar um plano", "Aggiungi un piano",
    ),
    "Mirror Subtool": (
        "Espejar subtool", "Symétriser le subtool", "Subtool spiegeln", "镜像子工具",
        "サブツールをミラー", "서브툴 미러", "Espelhar subtool", "Specchia subtool",
    ),
    "Creates a mirrored copy of the active subtool across an axis": (
        "Crea una copia reflejada del subtool activo sobre un eje",
        "Crée une copie en miroir du subtool actif selon un axe",
        "Erstellt eine gespiegelte Kopie des aktiven Subtools entlang einer Achse",
        "沿某个轴创建当前子工具的镜像副本",
        "アクティブなサブツールの鏡像コピーを軸に沿って作成します",
        "활성 서브툴의 미러 복사본을 축을 기준으로 만듭니다",
        "Cria uma cópia espelhada do subtool ativo em um eixo",
        "Crea una copia speculare del subtool attivo su un asse",
    ),
    "Mirror across the X axis": (
        "Reflejar en el eje X", "Miroir selon l'axe X", "An der X-Achse spiegeln",
        "沿 X 轴镜像", "X軸でミラー", "X축 기준 미러",
        "Espelhar no eixo X", "Specchia sull'asse X",
    ),
    "Mirror across the Y axis": (
        "Reflejar en el eje Y", "Miroir selon l'axe Y", "An der Y-Achse spiegeln",
        "沿 Y 轴镜像", "Y軸でミラー", "Y축 기준 미러",
        "Espelhar no eixo Y", "Specchia sull'asse Y",
    ),
    "Mirror across the Z axis": (
        "Reflejar en el eje Z", "Miroir selon l'axe Z", "An der Z-Achse spiegeln",
        "沿 Z 轴镜像", "Z軸でミラー", "Z축 기준 미러",
        "Espelhar no eixo Z", "Specchia sull'asse Z",
    ),
    "Show All Subtools": (
        "Mostrar todos", "Tout afficher", "Alle anzeigen", "全部显示",
        "すべて表示", "모두 표시", "Mostrar todos", "Mostra tutti",
    ),
    "Shows all the Tool's subtools and turns off Solo": (
        "Muestra todos los subtools del Tool y desactiva el Solo",
        "Affiche tous les subtools du Tool et désactive le Solo",
        "Zeigt alle Subtools des Tools und schaltet Solo aus",
        "显示 Tool 的所有子工具并关闭独显",
        "Tool のすべてのサブツールを表示し、ソロを解除します",
        "Tool의 모든 서브툴을 표시하고 솔로를 해제합니다",
        "Mostra todos os subtools do Tool e desativa o Solo",
        "Mostra tutti i subtool del Tool e disattiva il Solo",
    ),
    "Frame Active": (
        "Enmarcar activo", "Cadrer l'actif", "Aktives einrahmen", "框显当前项",
        "アクティブをフレーム表示", "활성 항목 화면에 맞추기",
        "Enquadrar ativo", "Inquadra attivo",
    ),
    "Frames the view on the active subtool": (
        "Encuadra la vista sobre el subtool activo",
        "Cadre la vue sur le subtool actif",
        "Richtet die Ansicht auf das aktive Subtool aus",
        "将视图对准当前子工具",
        "アクティブなサブツールにビューを合わせます",
        "활성 서브툴에 뷰를 맞춥니다",
        "Enquadra a vista no subtool ativo",
        "Inquadra la vista sul subtool attivo",
    ),
    "Split by Face Sets": (
        "Separar por Face Sets", "Séparer par Face Sets", "Nach Face Sets aufteilen",
        "按面组拆分", "面セットで分割", "페이스 셋으로 나누기",
        "Separar por Face Sets", "Separa per Face Set",
    ),
    "Splits the active subtool into one subtool per Face Set": (
        "Separa el subtool activo en un subtool por cada Face Set",
        "Sépare le subtool actif en un subtool par Face Set",
        "Teilt das aktive Subtool in ein Subtool pro Face Set auf",
        "将当前子工具按每个面组拆分为子工具",
        "アクティブなサブツールを面セットごとのサブツールに分割します",
        "활성 서브툴을 페이스 셋마다 하나의 서브툴로 나눕니다",
        "Separa o subtool ativo em um subtool por Face Set",
        "Separa il subtool attivo in un subtool per ogni Face Set",
    ),
    "Split by Mask": (
        "Separar por máscara", "Séparer par masque", "Nach Maske aufteilen",
        "按遮罩拆分", "マスクで分割", "마스크로 나누기",
        "Separar por máscara", "Separa per maschera",
    ),
    "Splits the masked area of the active subtool into a new subtool": (
        "Separa la zona enmascarada del subtool activo a un subtool nuevo",
        "Sépare la zone masquée du subtool actif dans un nouveau subtool",
        "Trennt den maskierten Bereich des aktiven Subtools in ein neues Subtool",
        "将当前子工具的遮罩区域拆分为新子工具",
        "アクティブなサブツールのマスク領域を新しいサブツールに分離します",
        "활성 서브툴의 마스크된 영역을 새 서브툴로 분리합니다",
        "Separa a área mascarada do subtool ativo em um novo subtool",
        "Separa la zona mascherata del subtool attivo in un nuovo subtool",
    ),
    "Multires Level": (
        "Nivel Multires", "Niveau Multires", "Multires-Stufe", "多级细分级别",
        "マルチレゾのレベル", "멀티레즈 레벨", "Nível Multires", "Livello Multires",
    ),
    "Raises or lowers the Multires level of the active subtool": (
        "Sube o baja el nivel de Multires del subtool activo",
        "Monte ou descend le niveau Multires du subtool actif",
        "Erhöht oder verringert die Multires-Stufe des aktiven Subtools",
        "升高或降低当前子工具的多级细分级别",
        "アクティブなサブツールのマルチレゾレベルを上げ下げします",
        "활성 서브툴의 멀티레즈 레벨을 올리거나 내립니다",
        "Sobe ou desce o nível de Multires do subtool ativo",
        "Aumenta o diminuisce il livello Multires del subtool attivo",
    ),
    "Boolean Role": (
        "Rol booleano", "Rôle booléen", "Boolesche Rolle", "布尔角色",
        "ブーリアンのロール", "불리언 역할", "Papel booleano", "Ruolo booleano",
    ),
    "Sets this subtool's boolean role (click the active role to clear it)": (
        "Fija el rol booleano de este subtool (clic en el rol activo para quitarlo)",
        "Définit le rôle booléen de ce subtool (cliquez sur le rôle actif pour l'enlever)",
        "Legt die boolesche Rolle dieses Subtools fest (Klick auf die aktive Rolle entfernt sie)",
        "设置此子工具的布尔角色（点击当前角色可取消）",
        "このサブツールのブーリアンロールを設定します（アクティブなロールをクリックで解除）",
        "이 서브툴의 불리언 역할을 설정합니다 (활성 역할을 클릭하면 해제)",
        "Define o papel booleano deste subtool (clique no papel ativo para removê-lo)",
        "Imposta il ruolo booleano di questo subtool (clicca sul ruolo attivo per rimuoverlo)",
    ),
    "Live Boolean Preview": (
        "Preview booleano en vivo", "Aperçu booléen en direct", "Live-Boolean-Vorschau",
        "实时布尔预览", "ライブブーリアンプレビュー", "실시간 불리언 미리보기",
        "Preview booleano ao vivo", "Anteprima booleana live",
    ),
    "Toggles the Tool's live boolean preview": (
        "Activa/desactiva el preview en vivo de la booleana del Tool",
        "Active/désactive l'aperçu en direct du booléen du Tool",
        "Schaltet die Live-Boolean-Vorschau des Tools um",
        "启用/禁用 Tool 的实时布尔预览",
        "Tool のライブブーリアンプレビューをオン・オフします",
        "Tool의 실시간 불리언 미리보기를 켜거나 끕니다",
        "Ativa/desativa o preview ao vivo da booleana do Tool",
        "Attiva/disattiva l'anteprima live della booleana del Tool",
    ),
    "Bakes the boolean: applies the result and removes the operands": (
        "Hornea la booleana: aplica el resultado y elimina los operandos",
        "Cuit le booléen : applique le résultat et supprime les opérandes",
        "Backt den Boolean: wendet das Ergebnis an und entfernt die Operanden",
        "烘焙布尔：应用结果并删除操作对象",
        "ブーリアンをベイクします。結果を適用し、オペランドを削除します",
        "불리언을 굽습니다: 결과를 적용하고 피연산자를 제거합니다",
        "Faz o bake da booleana: aplica o resultado e remove os operandos",
        "Esegue il bake della booleana: applica il risultato e rimuove gli operandi",
    ),
    "Direct Boolean": (
        "Booleana directa", "Booléen direct", "Direkter Boolean", "直接布尔",
        "ダイレクトブーリアン", "직접 불리언", "Booleana direta", "Booleana diretta",
    ),
    "Direct boolean: applies the other selected subtools to the active one and deletes them": (
        "Booleana directa: aplica al subtool activo el resto de seleccionados y los borra",
        "Booléen direct : applique les autres subtools sélectionnés à l'actif puis les supprime",
        "Direkter Boolean: wendet die übrigen ausgewählten Subtools auf das aktive an und löscht sie",
        "直接布尔：将其余选中的子工具应用到当前子工具并删除它们",
        "ダイレクトブーリアン: 選択中の他のサブツールをアクティブに適用して削除します",
        "직접 불리언: 선택된 나머지 서브툴을 활성 서브툴에 적용하고 삭제합니다",
        "Booleana direta: aplica ao subtool ativo os demais selecionados e os apaga",
        "Booleana diretta: applica al subtool attivo gli altri selezionati e li elimina",
    ),
    "Union with the active": (
        "Unir al activo", "Unir à l'actif", "Mit dem aktiven vereinigen", "与当前项合并",
        "アクティブと合成", "활성 서브툴과 합집합", "Unir ao ativo", "Unisci all'attivo",
    ),
    "Subtract from the active": (
        "Restar del activo", "Soustraire de l'actif", "Vom aktiven abziehen",
        "从当前项中减去", "アクティブから減算", "활성 서브툴에서 빼기",
        "Subtrair do ativo", "Sottrai dall'attivo",
    ),
    "Intersection": (
        "Intersección", "Intersection", "Schnittmenge", "交集",
        "交差", "교집합", "Interseção", "Intersezione",
    ),
    "Keep the common volume": (
        "Dejar el volumen común", "Garder le volume commun",
        "Das gemeinsame Volumen behalten", "保留公共体积",
        "共通の体積を残す", "공통 볼륨만 남기기",
        "Manter o volume comum", "Mantieni il volume comune",
    ),
    "Rename Subtool": (
        "Renombrar subtool", "Renommer le subtool", "Subtool umbenennen", "重命名子工具",
        "サブツールの名前を変更", "서브툴 이름 바꾸기", "Renomear subtool", "Rinomina subtool",
    ),
    "Renames this subtool": (
        "Renombra este subtool", "Renomme ce subtool", "Benennt dieses Subtool um",
        "重命名此子工具", "このサブツールの名前を変更します", "이 서브툴의 이름을 바꿉니다",
        "Renomeia este subtool", "Rinomina questo subtool",
    ),
    # --- Mensajes (reports) ---
    "Subtool not found": (
        "Subtool no encontrado", "Subtool introuvable", "Subtool nicht gefunden",
        "未找到子工具", "サブツールが見つかりません", "서브툴을 찾을 수 없습니다",
        "Subtool não encontrado", "Subtool non trovato",
    ),
    "No other subtool to jump to": (
        "No hay otro subtool al que saltar",
        "Aucun autre subtool vers lequel basculer",
        "Kein anderes Subtool zum Wechseln",
        "没有其他可跳转的子工具",
        "移動できる他のサブツールがありません",
        "이동할 다른 서브툴이 없습니다",
        "Não há outro subtool para saltar",
        "Nessun altro subtool a cui passare",
    ),
    "Duplicated: {}": (
        "Duplicado: {}", "Dupliqué : {}", "Dupliziert: {}", "已复制：{}",
        "複製しました: {}", "복제됨: {}", "Duplicado: {}", "Duplicato: {}",
    ),
    "Subtool deleted": (
        "Subtool borrado", "Subtool supprimé", "Subtool gelöscht", "子工具已删除",
        "サブツールを削除しました", "서브툴이 삭제되었습니다",
        "Subtool apagado", "Subtool eliminato",
    ),
    "The subtool is already at the end": (
        "El subtool ya está en el extremo",
        "Le subtool est déjà à l'extrémité",
        "Das Subtool ist bereits am Ende",
        "子工具已在末端",
        "サブツールはすでに端にあります",
        "서브툴이 이미 끝에 있습니다",
        "O subtool já está na extremidade",
        "Il subtool è già all'estremità",
    ),
    "Group created: {}": (
        "Grupo creado: {}", "Groupe créé : {}", "Gruppe erstellt: {}", "已创建组：{}",
        "グループを作成しました: {}", "그룹 생성됨: {}",
        "Grupo criado: {}", "Gruppo creato: {}",
    ),
    "Group not found": (
        "Grupo no encontrado", "Groupe introuvable", "Gruppe nicht gefunden",
        "未找到组", "グループが見つかりません", "그룹을 찾을 수 없습니다",
        "Grupo não encontrado", "Gruppo non trovato",
    ),
    "Moved to {}": (
        "Movido a {}", "Déplacé vers {}", "Verschoben nach {}", "已移动到 {}",
        "{} へ移動しました", "{}(으)로 이동했습니다",
        "Movido para {}", "Spostato in {}",
    ),
    "Could not merge the subtools": (
        "No se pudieron unir los subtools",
        "Impossible de fusionner les subtools",
        "Die Subtools konnten nicht vereint werden",
        "无法合并子工具",
        "サブツールを統合できませんでした",
        "서브툴을 합칠 수 없습니다",
        "Não foi possível unir os subtools",
        "Impossibile unire i subtool",
    ),
    "Subtools merged; the Multires is not preserved when merging": (
        "Subtools unidos; el Multires no se conserva al unir",
        "Subtools fusionnés ; le Multires n'est pas conservé lors de la fusion",
        "Subtools vereint; der Multires bleibt beim Vereinen nicht erhalten",
        "子工具已合并；合并时不保留多级细分",
        "サブツールを統合しました。統合時にマルチレゾは保持されません",
        "서브툴을 합쳤습니다. 합칠 때 멀티레즈는 유지되지 않습니다",
        "Subtools unidos; o Multires não é preservado ao unir",
        "Subtool uniti; il Multires non viene conservato durante l'unione",
    ),
    "Subtools merged": (
        "Subtools unidos", "Subtools fusionnés", "Subtools vereint", "子工具已合并",
        "サブツールを統合しました", "서브툴을 합쳤습니다",
        "Subtools unidos", "Subtool uniti",
    ),
    "Split into {} subtools": (
        "Separado en {} subtools", "Séparé en {} subtools",
        "In {} Subtools aufgeteilt", "已拆分为 {} 个子工具",
        "{} 個のサブツールに分割しました", "{}개의 서브툴로 나눴습니다",
        "Separado em {} subtools", "Separato in {} subtool",
    ),
    "The subtool has no loose parts": (
        "El subtool no tiene partes sueltas",
        "Le subtool n'a pas de parties isolées",
        "Das Subtool hat keine losen Teile",
        "子工具没有松散块",
        "サブツールに分離パーツはありません",
        "서브툴에 분리된 부분이 없습니다",
        "O subtool não tem partes soltas",
        "Il subtool non ha parti separate",
    ),
    "Subtool added: {}": (
        "Subtool añadido: {}", "Subtool ajouté : {}", "Subtool hinzugefügt: {}",
        "已添加子工具：{}", "サブツールを追加しました: {}", "서브툴 추가됨: {}",
        "Subtool adicionado: {}", "Subtool aggiunto: {}",
    ),
    "Mirror created: {}": (
        "Espejo creado: {}", "Miroir créé : {}", "Spiegelung erstellt: {}",
        "已创建镜像：{}", "ミラーを作成しました: {}", "미러 생성됨: {}",
        "Espelho criado: {}", "Copia speculare creata: {}",
    ),
    "Could not frame: {}": (
        "No se pudo encuadrar: {}", "Impossible de cadrer : {}",
        "Einrahmen fehlgeschlagen: {}", "无法框显：{}",
        "フレーム表示できませんでした: {}", "화면에 맞출 수 없습니다: {}",
        "Não foi possível enquadrar: {}", "Impossibile inquadrare: {}",
    ),
    "The mesh has no Face Sets": (
        "La malla no tiene Face Sets", "Le maillage n'a pas de Face Sets",
        "Das Mesh hat keine Face Sets", "网格没有面组",
        "メッシュに面セットがありません", "메시에 페이스 셋이 없습니다",
        "A malha não tem Face Sets", "La mesh non ha Face Set",
    ),
    "There is only one Face Set: nothing to split": (
        "Solo hay un Face Set: nada que separar",
        "Il n'y a qu'un seul Face Set : rien à séparer",
        "Es gibt nur ein Face Set: nichts aufzuteilen",
        "只有一个面组：无需拆分",
        "面セットが1つしかないため、分割するものがありません",
        "페이스 셋이 하나뿐입니다: 나눌 것이 없습니다",
        "Há apenas um Face Set: nada para separar",
        "C'è un solo Face Set: niente da separare",
    ),
    "Split into {} subtools by Face Set": (
        "Separado en {} subtools por Face Set",
        "Séparé en {} subtools par Face Set",
        "In {} Subtools nach Face Set aufgeteilt",
        "已按面组拆分为 {} 个子工具",
        "面セットごとに {} 個のサブツールに分割しました",
        "페이스 셋별로 {}개의 서브툴로 나눴습니다",
        "Separado em {} subtools por Face Set",
        "Separato in {} subtool per Face Set",
    ),
    "The mesh has no Sculpt mask": (
        "La malla no tiene máscara de Sculpt",
        "Le maillage n'a pas de masque Sculpt",
        "Das Mesh hat keine Sculpt-Maske",
        "网格没有雕刻遮罩",
        "メッシュにスカルプトマスクがありません",
        "메시에 스컬프트 마스크가 없습니다",
        "A malha não tem máscara de Sculpt",
        "La mesh non ha una maschera Sculpt",
    ),
    "There is no masked area": (
        "No hay zona enmascarada", "Aucune zone masquée", "Kein maskierter Bereich",
        "没有遮罩区域", "マスクされた領域がありません", "마스크된 영역이 없습니다",
        "Não há área mascarada", "Nessuna zona mascherata",
    ),
    "The whole mesh is masked: nothing to split": (
        "Toda la malla está enmascarada: nada que separar",
        "Tout le maillage est masqué : rien à séparer",
        "Das gesamte Mesh ist maskiert: nichts aufzuteilen",
        "整个网格都被遮罩：无需拆分",
        "メッシュ全体がマスクされているため、分割するものがありません",
        "메시 전체가 마스크되어 있습니다: 나눌 것이 없습니다",
        "Toda a malha está mascarada: nada para separar",
        "L'intera mesh è mascherata: niente da separare",
    ),
    "Masked area split into a new subtool": (
        "Zona enmascarada separada a un subtool nuevo",
        "Zone masquée séparée dans un nouveau subtool",
        "Maskierter Bereich in ein neues Subtool getrennt",
        "遮罩区域已拆分为新子工具",
        "マスク領域を新しいサブツールに分離しました",
        "마스크된 영역을 새 서브툴로 분리했습니다",
        "Área mascarada separada em um novo subtool",
        "Zona mascherata separata in un nuovo subtool",
    ),
    "Mark at least one subtool as 'Add'": (
        "Marca al menos un subtool como 'Añadir'",
        "Marquez au moins un subtool comme « Ajouter »",
        "Markiere mindestens ein Subtool als 'Hinzufügen'",
        "至少将一个子工具标记为“添加”",
        "少なくとも1つのサブツールを「追加」に設定してください",
        "적어도 하나의 서브툴을 '추가'로 표시하세요",
        "Marque pelo menos um subtool como 'Adicionar'",
        "Contrassegna almeno un subtool come 'Aggiungi'",
    ),
    "Boolean preview: {} operands": (
        "Preview booleano: {} operandos", "Aperçu booléen : {} opérandes",
        "Boolean-Vorschau: {} Operanden", "布尔预览：{} 个操作对象",
        "ブーリアンプレビュー: オペランド {} 個", "불리언 미리보기: 피연산자 {}개",
        "Preview booleano: {} operandos", "Anteprima booleana: {} operandi",
    ),
    "Could not apply {}: {}": (
        "No se pudo aplicar {}: {}", "Impossible d'appliquer {} : {}",
        "{} konnte nicht angewendet werden: {}", "无法应用 {}：{}",
        "{} を適用できませんでした: {}", "{}을(를) 적용할 수 없습니다: {}",
        "Não foi possível aplicar {}: {}", "Impossibile applicare {}: {}",
    ),
    "Boolean applied": (
        "Booleana aplicada", "Booléen appliqué", "Boolean angewendet", "布尔已应用",
        "ブーリアンを適用しました", "불리언이 적용되었습니다",
        "Booleana aplicada", "Booleana applicata",
    ),
    "Select the active and at least one other subtool": (
        "Selecciona el activo y al menos otro subtool",
        "Sélectionnez l'actif et au moins un autre subtool",
        "Wähle das aktive und mindestens ein weiteres Subtool aus",
        "请选择当前子工具和至少一个其他子工具",
        "アクティブと少なくとも1つの他のサブツールを選択してください",
        "활성 서브툴과 적어도 하나의 다른 서브툴을 선택하세요",
        "Selecione o ativo e pelo menos outro subtool",
        "Seleziona l'attivo e almeno un altro subtool",
    ),
    "Some boolean was not applied (Multires in the active's stack?)": (
        "Alguna booleana no se aplicó (¿Multires en la pila del activo?)",
        "Un booléen n'a pas été appliqué (Multires dans la pile de l'actif ?)",
        "Ein Boolean wurde nicht angewendet (Multires im Stapel des aktiven?)",
        "某个布尔未能应用（当前对象的堆栈中有多级细分？）",
        "一部のブーリアンを適用できませんでした（アクティブのスタックにマルチレゾ？）",
        "일부 불리언이 적용되지 않았습니다 (활성 스택에 멀티레즈가 있나요?)",
        "Alguma booleana não foi aplicada (Multires na pilha do ativo?)",
        "Qualche booleana non è stata applicata (Multires nello stack dell'attivo?)",
    ),
    "Boolean {} applied": (
        "Booleana {} aplicada", "Booléen {} appliqué", "Boolean {} angewendet",
        "布尔 {} 已应用", "ブーリアン {} を適用しました", "불리언 {} 적용됨",
        "Booleana {} aplicada", "Booleana {} applicata",
    ),
    # --- Miniaturas (preview.py) ---
    "Refresh Thumbnails": (
        "Refrescar miniaturas", "Rafraîchir les vignettes",
        "Vorschaubilder aktualisieren", "刷新缩略图",
        "サムネイルを更新", "썸네일 새로 고침",
        "Atualizar miniaturas", "Aggiorna miniature",
    ),
    "Regenerates the thumbnails of all the active Tool's subtools": (
        "Regenera las miniaturas de todos los subtools del Tool activo",
        "Régénère les vignettes de tous les subtools du Tool actif",
        "Erzeugt die Vorschaubilder aller Subtools des aktiven Tools neu",
        "重新生成当前 Tool 所有子工具的缩略图",
        "アクティブな Tool の全サブツールのサムネイルを再生成します",
        "활성 Tool의 모든 서브툴 썸네일을 다시 생성합니다",
        "Regenera as miniaturas de todos os subtools do Tool ativo",
        "Rigenera le miniature di tutti i subtool del Tool attivo",
    ),
    "Thumbnails require a GPU (not in background)": (
        "Las miniaturas necesitan GPU (no en background)",
        "Les vignettes nécessitent un GPU (pas en arrière-plan)",
        "Vorschaubilder benötigen eine GPU (nicht im Hintergrundmodus)",
        "缩略图需要 GPU（后台模式不可用）",
        "サムネイルには GPU が必要です（バックグラウンドでは不可）",
        "썸네일에는 GPU가 필요합니다 (백그라운드에서는 불가)",
        "As miniaturas precisam de GPU (não em background)",
        "Le miniature richiedono una GPU (non in background)",
    ),
    "Could not generate any thumbnail": (
        "No se pudo generar ninguna miniatura",
        "Impossible de générer une vignette",
        "Es konnte kein Vorschaubild erzeugt werden",
        "无法生成任何缩略图",
        "サムネイルを生成できませんでした",
        "썸네일을 생성할 수 없습니다",
        "Não foi possível gerar nenhuma miniatura",
        "Impossibile generare alcuna miniatura",
    ),
    "{} thumbnails updated": (
        "{} miniaturas actualizadas", "{} vignettes mises à jour",
        "{} Vorschaubilder aktualisiert", "已更新 {} 个缩略图",
        "{} 件のサムネイルを更新しました", "썸네일 {}개 업데이트됨",
        "{} miniaturas atualizadas", "{} miniature aggiornate",
    ),
    # --- Propiedades (properties.py) ---
    "Order": (
        "Orden", "Ordre", "Reihenfolge", "顺序",
        "順序", "순서", "Ordem", "Ordine",
    ),
    "Position of the subtool within its group": (
        "Posición del subtool dentro de su grupo",
        "Position du subtool dans son groupe",
        "Position des Subtools in seiner Gruppe",
        "子工具在组内的位置",
        "グループ内でのサブツールの位置",
        "그룹 안에서 서브툴의 위치",
        "Posição do subtool dentro do seu grupo",
        "Posizione del subtool nel suo gruppo",
    ),
    "Previously Hidden": (
        "Oculto previo", "Masqué précédemment", "Zuvor verborgen", "先前隐藏",
        "以前の非表示状態", "이전 숨김 상태",
        "Oculto anterior", "Nascosto in precedenza",
    ),
    "Visibility snapshot to restore after leaving Solo": (
        "Snapshot de visibilidad para restaurar tras salir de Solo",
        "Instantané de visibilité à restaurer après avoir quitté le Solo",
        "Sichtbarkeits-Snapshot zum Wiederherstellen nach dem Solo",
        "退出独显后用于恢复的可见性快照",
        "ソロ解除後に復元するための表示状態のスナップショット",
        "솔로 해제 후 복원할 표시 상태 스냅숏",
        "Snapshot de visibilidade para restaurar após sair do Solo",
        "Snapshot di visibilità da ripristinare dopo l'uscita dal Solo",
    ),
    "How this subtool participates in the live boolean": (
        "Cómo participa este subtool en la booleana en vivo",
        "Comment ce subtool participe au booléen en direct",
        "Wie dieses Subtool am Live-Boolean teilnimmt",
        "此子工具参与实时布尔的方式",
        "このサブツールがライブブーリアンにどう関わるか",
        "이 서브툴이 실시간 불리언에 참여하는 방식",
        "Como este subtool participa da booleana ao vivo",
        "Come questo subtool partecipa alla booleana live",
    ),
    "None": (
        "Ninguno", "Aucun", "Keine", "无",
        "なし", "없음", "Nenhum", "Nessuno",
    ),
    "Does not participate in the boolean": (
        "No participa en la booleana",
        "Ne participe pas au booléen",
        "Nimmt nicht am Boolean teil",
        "不参与布尔",
        "ブーリアンに参加しません",
        "불리언에 참여하지 않습니다",
        "Não participa da booleana",
        "Non partecipa alla booleana",
    ),
    "Joins the result (union)": (
        "Se une al resultado (unión)",
        "S'ajoute au résultat (union)",
        "Wird mit dem Ergebnis vereinigt (Vereinigung)",
        "并入结果（并集）",
        "結果に合成されます（合成）",
        "결과에 합쳐집니다 (합집합)",
        "Une-se ao resultado (união)",
        "Si unisce al risultato (unione)",
    ),
    "Subtract": (
        "Restar", "Soustraire", "Abziehen", "相减",
        "減算", "빼기", "Subtrair", "Sottrai",
    ),
    "Is subtracted from the result (difference)": (
        "Se resta del resultado (diferencia)",
        "Est soustrait du résultat (différence)",
        "Wird vom Ergebnis abgezogen (Differenz)",
        "从结果中减去（差集）",
        "結果から減算されます（差分）",
        "결과에서 빼집니다 (차집합)",
        "É subtraído do resultado (diferença)",
        "Viene sottratto dal risultato (differenza)",
    ),
    "Keeps only the common volume (intersection)": (
        "Deja solo el volumen común (intersección)",
        "Ne garde que le volume commun (intersection)",
        "Behält nur das gemeinsame Volumen (Schnittmenge)",
        "仅保留公共体积（交集）",
        "共通の体積だけを残します（交差）",
        "공통 볼륨만 남깁니다 (교집합)",
        "Mantém apenas o volume comum (interseção)",
        "Mantiene solo il volume comune (intersezione)",
    ),
    "Boolean Result": (
        "Resultado booleano", "Résultat booléen", "Boolean-Ergebnis", "布尔结果",
        "ブーリアンの結果", "불리언 결과", "Resultado booleano", "Risultato booleano",
    ),
    "Marks the live preview result object": (
        "Marca el objeto de resultado del preview en vivo",
        "Marque l'objet résultat de l'aperçu en direct",
        "Markiert das Ergebnisobjekt der Live-Vorschau",
        "标记实时预览的结果对象",
        "ライブプレビューの結果オブジェクトを示します",
        "실시간 미리보기의 결과 오브젝트를 표시합니다",
        "Marca o objeto de resultado do preview ao vivo",
        "Contrassegna l'oggetto risultato dell'anteprima live",
    ),
    "Expanded": (
        "Expandido", "Déplié", "Ausgeklappt", "已展开",
        "展開", "펼침", "Expandido", "Espanso",
    ),
    "Whether the group is expanded in the palette": (
        "Si el grupo está desplegado en la paleta",
        "Si le groupe est déplié dans la palette",
        "Ob die Gruppe in der Palette ausgeklappt ist",
        "组是否在面板中展开",
        "グループがパレットで展開されているかどうか",
        "그룹이 팔레트에서 펼쳐져 있는지 여부",
        "Se o grupo está expandido na paleta",
        "Se il gruppo è espanso nella palette",
    ),
    "Active Solo": (
        "Solo activo", "Solo actif", "Aktives Solo", "当前独显",
        "アクティブなソロ", "활성 솔로", "Solo ativo", "Solo attivo",
    ),
    "Name of the isolated subtool (empty = no Solo)": (
        "Nombre del subtool aislado (vacío = sin Solo)",
        "Nom du subtool isolé (vide = pas de Solo)",
        "Name des isolierten Subtools (leer = kein Solo)",
        "被隔离子工具的名称（空 = 无独显）",
        "分離表示中のサブツール名（空 = ソロなし）",
        "격리된 서브툴의 이름 (비어 있음 = 솔로 없음)",
        "Nome do subtool isolado (vazio = sem Solo)",
        "Nome del subtool isolato (vuoto = nessun Solo)",
    ),
    "Boolean Preview": (
        "Preview booleano", "Aperçu booléen", "Boolean-Vorschau", "布尔预览",
        "ブーリアンプレビュー", "불리언 미리보기",
        "Preview booleano", "Anteprima booleana",
    ),
    "Name of the preview result object (empty = no preview)": (
        "Nombre del objeto de resultado del preview (vacío = sin preview)",
        "Nom de l'objet résultat de l'aperçu (vide = pas d'aperçu)",
        "Name des Vorschau-Ergebnisobjekts (leer = keine Vorschau)",
        "预览结果对象的名称（空 = 无预览）",
        "プレビュー結果オブジェクトの名前（空 = プレビューなし）",
        "미리보기 결과 오브젝트의 이름 (비어 있음 = 미리보기 없음)",
        "Nome do objeto de resultado do preview (vazio = sem preview)",
        "Nome dell'oggetto risultato dell'anteprima (vuoto = nessuna anteprima)",
    ),
    # --- Preferencias ---
    "Re-enter Sculpt when Jumping": (
        "Reentrar en Sculpt al saltar",
        "Revenir en Sculpt lors du saut",
        "Beim Wechseln wieder in Sculpt",
        "跳转时重新进入雕刻模式",
        "切り替え時にスカルプトへ再突入",
        "이동 시 스컬프트 재진입",
        "Reentrar no Sculpt ao saltar",
        "Rientra in Sculpt al salto",
    ),
    "When activating another subtool from Sculpt, return to Sculpt mode "
    "(if disabled, the jump leaves the object in Object mode)": (
        "Al activar otro subtool desde Sculpt, volver a modo Sculpt "
        "(si se desactiva, el salto deja el objeto en modo Objeto)",
        "En activant un autre subtool depuis Sculpt, revenir en mode Sculpt "
        "(si désactivé, le saut laisse l'objet en mode Objet)",
        "Beim Aktivieren eines anderen Subtools aus Sculpt in den Sculpt-Modus "
        "zurückkehren (deaktiviert bleibt das Objekt im Objektmodus)",
        "从雕刻模式激活其他子工具时返回雕刻模式（禁用时跳转后对象保持物体模式）",
        "スカルプト中に別のサブツールをアクティブにしたときスカルプトモードに戻ります"
        "（無効の場合はオブジェクトモードのまま）",
        "스컬프트에서 다른 서브툴을 활성화할 때 스컬프트 모드로 돌아갑니다 "
        "(비활성화하면 오브젝트 모드로 남습니다)",
        "Ao ativar outro subtool a partir do Sculpt, voltar ao modo Sculpt "
        "(se desativado, o salto deixa o objeto no modo Objeto)",
        "Attivando un altro subtool da Sculpt, torna in modalità Sculpt "
        "(se disattivato, il salto lascia l'oggetto in modalità Oggetto)",
    ),
    "Solo Includes the Group": (
        "Solo incluye el grupo", "Le Solo inclut le groupe",
        "Solo schließt die Gruppe ein", "独显包含组",
        "ソロにグループを含める", "솔로에 그룹 포함",
        "Solo inclui o grupo", "Il Solo include il gruppo",
    ),
    "When isolating (Solo), keep the subtool's whole group visible, not just the object": (
        "Al aislar (Solo), mantener visible todo el grupo del subtool, no solo el objeto",
        "Lors de l'isolement (Solo), garder visible tout le groupe du subtool, "
        "pas seulement l'objet",
        "Beim Isolieren (Solo) die ganze Gruppe des Subtools sichtbar lassen, "
        "nicht nur das Objekt",
        "隔离（独显）时保持子工具所在整个组可见，而不仅是该对象",
        "分離表示（ソロ）時に、オブジェクトだけでなくサブツールのグループ全体を表示したままにします",
        "격리(솔로) 시 오브젝트만이 아니라 서브툴의 그룹 전체를 표시합니다",
        "Ao isolar (Solo), manter visível todo o grupo do subtool, não só o objeto",
        "Quando isoli (Solo), mantieni visibile l'intero gruppo del subtool, "
        "non solo l'oggetto",
    ),
    "Confirm Delete": (
        "Confirmar borrado", "Confirmer la suppression", "Löschen bestätigen",
        "确认删除", "削除の確認", "삭제 확인",
        "Confirmar exclusão", "Conferma eliminazione",
    ),
    "Asks for confirmation before deleting a subtool": (
        "Pedir confirmación antes de borrar un subtool",
        "Demande confirmation avant de supprimer un subtool",
        "Fragt vor dem Löschen eines Subtools nach Bestätigung",
        "删除子工具前要求确认",
        "サブツールを削除する前に確認します",
        "서브툴을 삭제하기 전에 확인을 요청합니다",
        "Pede confirmação antes de apagar um subtool",
        "Chiede conferma prima di eliminare un subtool",
    ),
    "Confirm Merge": (
        "Confirmar unión", "Confirmer la fusion", "Vereinen bestätigen",
        "确认合并", "統合の確認", "합치기 확인",
        "Confirmar união", "Conferma unione",
    ),
    "Asks for confirmation before merging subtools": (
        "Pedir confirmación antes de unir subtools",
        "Demande confirmation avant de fusionner des subtools",
        "Fragt vor dem Vereinen von Subtools nach Bestätigung",
        "合并子工具前要求确认",
        "サブツールを統合する前に確認します",
        "서브툴을 합치기 전에 확인을 요청합니다",
        "Pede confirmação antes de unir subtools",
        "Chiede conferma prima di unire i subtool",
    ),
    "Enable Hotkeys": (
        "Activar atajos", "Activer les raccourcis", "Tastenkürzel aktivieren",
        "启用快捷键", "ショートカットを有効化", "단축키 활성화",
        "Ativar atalhos", "Attiva scorciatoie",
    ),
    "Registers the hotkeys to cycle subtools (Alt+↑ / Alt+↓)": (
        "Registrar los atajos para ciclar subtools (Alt+↑ / Alt+↓)",
        "Enregistre les raccourcis pour parcourir les subtools (Alt+↑ / Alt+↓)",
        "Registriert die Tastenkürzel zum Wechseln der Subtools (Alt+↑ / Alt+↓)",
        "注册循环切换子工具的快捷键（Alt+↑ / Alt+↓）",
        "サブツールを切り替えるショートカットを登録します（Alt+↑ / Alt+↓）",
        "서브툴을 순환하는 단축키를 등록합니다 (Alt+↑ / Alt+↓)",
        "Registra os atalhos para alternar subtools (Alt+↑ / Alt+↓)",
        "Registra le scorciatoie per ciclare i subtool (Alt+↑ / Alt+↓)",
    ),
    "List Order": (
        "Orden de la lista", "Ordre de la liste", "Listenreihenfolge", "列表顺序",
        "リストの順序", "목록 순서", "Ordem da lista", "Ordine dell'elenco",
    ),
    "How to sort the subtools within each group": (
        "Cómo ordenar los subtools dentro de cada grupo",
        "Comment trier les subtools dans chaque groupe",
        "Wie die Subtools in jeder Gruppe sortiert werden",
        "每个组内子工具的排序方式",
        "各グループ内でのサブツールの並べ方",
        "각 그룹 안에서 서브툴을 정렬하는 방식",
        "Como ordenar os subtools dentro de cada grupo",
        "Come ordinare i subtool in ogni gruppo",
    ),
    "By the assigned order (move up/down)": (
        "Por el orden asignado (subir/bajar)",
        "Selon l'ordre assigné (monter/descendre)",
        "Nach der zugewiesenen Reihenfolge (hoch/runter)",
        "按指定顺序（上移/下移）",
        "割り当てた順序で（上へ／下へ）",
        "지정된 순서대로 (위로/아래로)",
        "Pela ordem atribuída (subir/descer)",
        "Secondo l'ordine assegnato (su/giù)",
    ),
    "Alphabetical by name": (
        "Alfabético por nombre", "Alphabétique par nom", "Alphabetisch nach Name",
        "按名称字母排序", "名前のアルファベット順", "이름 알파벳순",
        "Alfabética por nome", "Alfabetico per nome",
    ),
    "Show Thumbnails": (
        "Mostrar miniaturas", "Afficher les vignettes", "Vorschaubilder anzeigen",
        "显示缩略图", "サムネイルを表示", "썸네일 표시",
        "Mostrar miniaturas", "Mostra miniature",
    ),
    "Draws a thumbnail of each subtool in the palette (ZBrush style). Requires GPU": (
        "Dibujar una miniatura de cada subtool en la paleta (estilo ZBrush). Requiere GPU",
        "Dessine une vignette de chaque subtool dans la palette (style ZBrush). "
        "Nécessite un GPU",
        "Zeichnet ein Vorschaubild jedes Subtools in der Palette (ZBrush-Stil). "
        "Benötigt GPU",
        "在面板中为每个子工具绘制缩略图（ZBrush 风格）。需要 GPU",
        "パレットに各サブツールのサムネイルを描画します（ZBrush スタイル）。GPU が必要です",
        "팔레트에 각 서브툴의 썸네일을 그립니다 (ZBrush 스타일). GPU 필요",
        "Desenha uma miniatura de cada subtool na paleta (estilo ZBrush). Requer GPU",
        "Disegna una miniatura di ogni subtool nella palette (stile ZBrush). Richiede GPU",
    ),
    "Automatic Thumbnails": (
        "Miniaturas automáticas", "Vignettes automatiques",
        "Automatische Vorschaubilder", "自动缩略图",
        "自動サムネイル", "자동 썸네일",
        "Miniaturas automáticas", "Miniature automatiche",
    ),
    "Regenerates the thumbnail automatically: when creating a mesh, switching "
    "the active subtool, reordering, and periodically. Disable it if sculpting stutters": (
        "Regenerar la miniatura automáticamente: al crear una malla, cambiar de "
        "subtool activo, reordenar y cada cierto tiempo. Desactívalo si notas "
        "tirones al esculpir",
        "Régénère la vignette automatiquement : à la création d'un maillage, au "
        "changement de subtool actif, au réordonnancement et périodiquement. "
        "Désactivez-le en cas de saccades en sculptant",
        "Erzeugt das Vorschaubild automatisch neu: beim Erstellen eines Meshes, "
        "beim Wechsel des aktiven Subtools, beim Umsortieren und in Intervallen. "
        "Deaktivieren, falls das Sculpten ruckelt",
        "自动重新生成缩略图：创建网格、切换活动子工具、重新排序时及定期执行。"
        "若雕刻时卡顿请禁用",
        "サムネイルを自動的に再生成します: メッシュ作成時、アクティブサブツール切替時、"
        "並べ替え時、および定期的に。スカルプト中にカクつく場合は無効にしてください",
        "썸네일을 자동으로 다시 생성합니다: 메시 생성, 활성 서브툴 변경, 재정렬 시 및 "
        "주기적으로. 스컬프팅이 끊기면 비활성화하세요",
        "Regenera a miniatura automaticamente: ao criar uma malha, mudar o subtool "
        "ativo, reordenar e periodicamente. Desative se notar travamentos ao esculpir",
        "Rigenera la miniatura automaticamente: alla creazione di una mesh, al cambio "
        "di subtool attivo, al riordino e periodicamente. Disattivalo se noti scatti "
        "mentre scolpisci",
    ),
    "Automatic Interval (s)": (
        "Intervalo automático (s)", "Intervalle automatique (s)",
        "Automatisches Intervall (s)", "自动间隔（秒）",
        "自動間隔（秒）", "자동 간격(초)",
        "Intervalo automático (s)", "Intervallo automatico (s)",
    ),
    "How many seconds between recaptures of the active subtool's thumbnail "
    "if no other event has occurred": (
        "Cada cuántos segundos recapturar la miniatura del subtool activo si no "
        "ha ocurrido ningún otro evento",
        "Toutes les combien de secondes recapturer la vignette du subtool actif "
        "si aucun autre événement ne s'est produit",
        "Alle wie viel Sekunden das Vorschaubild des aktiven Subtools neu "
        "aufgenommen wird, wenn kein anderes Ereignis eingetreten ist",
        "若无其他事件，每隔多少秒重新捕捉活动子工具的缩略图",
        "他のイベントがない場合に、アクティブサブツールのサムネイルを再取得する間隔（秒）",
        "다른 이벤트가 없을 때 활성 서브툴의 썸네일을 다시 캡처하는 간격(초)",
        "A cada quantos segundos recapturar a miniatura do subtool ativo se "
        "nenhum outro evento ocorreu",
        "Ogni quanti secondi ricatturare la miniatura del subtool attivo se non "
        "è avvenuto nessun altro evento",
    ),
    "Thumbnail Size": (
        "Tamaño de miniatura", "Taille des vignettes", "Vorschaubildgröße",
        "缩略图大小", "サムネイルのサイズ", "썸네일 크기",
        "Tamanho da miniatura", "Dimensione miniatura",
    ),
    "Scale of the thumbnail in the palette": (
        "Escala de la miniatura en la paleta",
        "Échelle de la vignette dans la palette",
        "Skalierung des Vorschaubilds in der Palette",
        "面板中缩略图的缩放",
        "パレット内のサムネイルの拡大率",
        "팔레트에서 썸네일의 크기 배율",
        "Escala da miniatura na paleta",
        "Scala della miniatura nella palette",
    ),
}


def _build() -> dict:
    """Expande _STRINGS al formato {locale: {(contexto, msgid): traducción}}."""
    data = {}
    for index, locale in enumerate(_LOCALES):
        entries = {}
        for msgid, translations in _STRINGS.items():
            for context in _CONTEXTS:
                entries[(context, msgid)] = translations[index]
        data[locale] = entries
    for alias, source in _ALIASES.items():
        data[alias] = data[source]
    return data


def register():
    bpy.app.translations.register(__package__, _build())


def unregister():
    bpy.app.translations.unregister(__package__)
