/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) {
            return NULL;
        }

        TreeNode *left = invertTree(root->left);
        TreeNode *right = invertTree(root->right);

        TreeNode *temp = left;
        root->left = right;
        root->right = temp;

        return root;
    }
};

//                 1
//        2                 3
//    4        5        6
//                  7        8




