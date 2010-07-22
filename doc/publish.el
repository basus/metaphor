(require 'org-publish)
(setq org-publish-project-alist
      '(
        ("to-html"
         :base-directory "~/src/metaphor/doc/org"
         :base-extension "org"
         :publishing-directory "~/src/metaphor/doc/html"
         :link-home "~/src/metaphor/doc/html/index.html"
         :link-up "~/src/metaphor/doc/html/index.html"
         :recursive t
         :publishing-function org-publish-org-to-html
         :exclude "level-0.org"
         :headline-levels 4
         :table-of-contents: nil
         :auto-preamble t
         :auto-postamble nil
         )
        ("metaphor" :components ("to-html"))
        ))
